#this is the server code that handles routing and services for auction page

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import os

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
    return render_template('auction/auctionItem.html',image_urls=assetUrlList)#url list is iterated inside the html file using python scripts, view auctionItem.html to see more
