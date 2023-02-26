#this is the server code that handles routing and services for auction page

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os

from TLM2008_Project.db import get_db
import datetime

#define blueprint to register with app upon startup
auctionBp = Blueprint('auction',__name__,url_prefix='/auction')
print("Initializing auction.py...")

#function extension to route auction request for render of auction front page
@auctionBp.route('/')
def mainPage():
    return render_template('auction/auctionMain.html')

#function extension to route auction item request and render images of the item series for auctionItem.html
@auctionBp.route('/auctionItem/<item>/') #<item> is a variable that stores the last resource request from client and is passed into function as an argument
def itemPage(item):
    itemInfoRow = retrieveItemInfo(item)
    itemInfoList = dict(itemInfoRow)
    itemInfoList["item_current_price"] = int(itemInfoList["item_current_price"]) + sumCurrentBids(itemInfoList["item_id"])
    print(itemInfoList)
    count = 0
    assetUrlList = []
    asset_extension = ".webp"
    assetDir= "TLM2008_Project/static/img/POPtrade/WHAT_I_USED/"+item+"/"   #assetDir and assetPath is different as os.listdir works on entire folder structure while html render works inside static folder
    assetPath = "img/POPtrade/WHAT_I_USED/"+item+"/"
    for assetName in os.listdir(assetDir):      #iterates through every asset inside directory
        if assetName.endswith(asset_extension):
            count +=1       #increment count whenever asset is detected
    while(count!=0):
        mergeTuple = (assetPath,str(count),asset_extension)
        outPut = "".join(mergeTuple)
        indexedOutPut = (count,outPut)
        assetUrlList.append(indexedOutPut)     #create list of static url for client
        print(indexedOutPut)
        count -=1
    return render_template('auction/auctionItem.html',image_urls=assetUrlList,itemInfo = itemInfoList)#url list is iterated inside the html file using python scripts, view auctionItem.html to see more

@auctionBp.route('/auctionItem/bid/<item>/',methods=('GET', 'POST'))
def bidPage(item):
    print(item)
    print("Bid page is accessed by user: "+request.form['bidder'])
    print("Redirecting to login page...")
    if(request.form['bidder'] =="Guest"):
        return redirect(url_for('auth.login_register'))
    
    if request.method == 'POST':
        username = request.form['bidder']
        bidValue = request.form['bidValue']
        item_id = request.form['item_id']
        print("Bid value of: "+bidValue + " is received from user: "+username)
        transactionDate = datetime.datetime.now()
        auctionId = item+username+str(transactionDate)
        db = get_db()
        try:
            #if details not used, create entry into database, else return error to client
            db.execute(
                "INSERT INTO auction_bids (auction_id, user_id, bid_amount, transaction_date,item_id) VALUES (?, ?, ?, ?,?)",
                (auctionId,username, bidValue, transactionDate,item_id),
            )
            db.commit()
            return redirect(url_for('auction.itemPage',item=item))
        except db.DataError:
            error = f"There's an error with the database."
        flash(error)
        
    return render_template('auction/bid.html')

def retrieveItemInfo(item):
    db = get_db()
    itemInfo = db.execute(
        "SELECT * FROM auction_item WHERE item_name = ?",(item,)
    ).fetchone()
    return itemInfo

def sumCurrentBids(item):
    db = get_db()
    sumOfBids = db.execute(
        "SELECT SUM(bid_amount) FROM auction_bids WHERE item_id = ?",(item,)
    ).fetchone()
    #print("retrieved values: " + str(sumOfBids[0]))
    return sumOfBids[0]