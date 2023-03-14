from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

import os

from TLM2008_Project.db import get_db

marketBp = Blueprint('marketplace',__name__,url_prefix='/marketplace')
print("Initializing market.py...")

# @itemBp.route('/')
# def itemPage():
#     return render_template("""Jurassic_World_series""")

@marketBp.route("/")
def mainPage():
    allItemInfo = []
    dbItemInfo = retriveAllItemInfo()
    for stuff in dbItemInfo:
        stuff = dict(stuff)
        stuff['url'] = "/marketplace/marketplaceItem/{}/".format(stuff['item_id'])
        allItemInfo.append(stuff)
    #print(allItemInfo)
    return render_template("/marketplace/Marketplace.html",allItemInfo = allItemInfo)

@marketBp.route("/marketplaceItem/<item>/")
def itemPage(item):
    try:
        itemInfoRow = retrieveItemInfo(item)
        itemInfoDict = dict(itemInfoRow)
        #print(itemInfoDict)
    except:
        print("Error retrieving item info from database")
    count = 0
    assetUrlList = []
    asset_extension = ".webp"
    assetDir= "TLM2008_Project/static/img/POPtrade/WHAT_I_USED/"+itemInfoDict['item_name']+"/"   #assetDir and assetPath is different as os.listdir works on entire folder structure while html render works inside static folder
    assetPath = "img/POPtrade/WHAT_I_USED/"+itemInfoDict['item_name']+"/"
    for assetName in os.listdir(assetDir):      #iterates through every asset inside directory
        if assetName.endswith(asset_extension):
            count +=1       #increment count whenever asset is detected
    while(count!=0):
        mergeTuple = (assetPath,str(count),asset_extension)
        outPut = "".join(mergeTuple)
        indexedOutPut = (count,outPut)
        assetUrlList.append(indexedOutPut)     #create list of static url for client
        #print(indexedOutPut)
        count -=1
    print("Asset URL:")
    print(assetUrlList)
    print("Item Info:")
    print(itemInfoDict)
    return render_template('marketplace/marketplaceItem.html',image_urls=assetUrlList,itemInfo = itemInfoDict)

def retriveAllItemInfo():
    db = get_db()
    itemInfo = db.execute(
        "SELECT * FROM listed_item where item_catergory = 'market'"
    ).fetchall()
    return itemInfo

def retrieveItemInfo(item):
    db = get_db()
    itemInfo = db.execute(
        "SELECT * FROM listed_item WHERE item_id = ?",(item,)
    ).fetchone()
    return itemInfo
