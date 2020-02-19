# This script is constantly running on the google machine,
# It pulls the data from the rsbuddy api and enters it into the sql data base in the google cloud
# It also starts a threading timer to run the function to collect data in another six minutes,
# each thread spawns another one keeping the data flowing

import mysql.connector
from datetime import datetime, timezone, timedelta
import requests
import json
import threading
import time

def collectData():
    thread = threading.Timer(360, collectData) #start another thread to collect data in 6 minutes
    print("Starting Next Thread")#debug
    thread.start()
    print("connecting to database")#debug
    mydb = mysql.connector.connect(
        host = "redacted",
        user = 'root',
        password = 'redacted',
        database = 'index')
    myCursor = mydb.cursor() #cursor used to interact with the database
    
    timeToExtract =int( datetime.utcnow().timestamp()*1000) #current time, used to query rsbuddy api
    URL = "https://rsbuddy.com/exchange/summary.json?ts=" + str(timeToExtract)
    data = requests.get(url = URL, params = {}).json() #get the data from rsbuddy
    print("recieved Data") #debug
    myCursor.execute("SELECT id FROM items") #query for a list of items in the database, used to check for new items
    knownItems = myCursor.fetchall()
    print("recieved known items") #debug
    vals = []
    for item in data:
        thisItem = data[item]
        if ((thisItem["id"],) in knownItems): #if item is already in database, then append data points to be inserted into the database
            vals.append((timeToExtract, thisItem["id"], thisItem["sell_average"], thisItem["sell_quantity"], thisItem["buy_average"], thisItem["buy_quantity"], thisItem["overall_average"], this$
        else: #if it's not in the database then add this item into the item database before updating the vals array
            print("New Item id: " + str(thisItem["id"]))
            try:
                myCursor.execute("INSERT INTO items (id, name, members) VALUES (%s, %s, %s)", (thisItem["id"], thisItem["name"], thisItem["members"]))
                mydb.commit()
                vals.append((timeToExtract, thisItem["id"], thisItem["sell_average"], thisItem["sell_quantity"], thisItem["buy_average"], thisItem["buy_quantity"], thisItem["overall_average"], $
            except:
                print("Unable to insert new Item")
    sql = "INSERT INTO data (time, itemID, sellAvg, sellQuant, buyAvg, buyQuant, overallAvg, overallQuant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    try:
        myCursor.executemany(sql, vals) #this executes the sql command over every row in the vals array
        mydb.commit()
        print("Data Commited with timestamp: " + str(timeToExtract)) #debug
    except Exception as E:
        print("Error inserting data: " + E) #debug hopefully this never happens cause that'd be unfortunate
    
timeToExtract = datetime.utcnow() #this executes once when the program is first run, it waits till the time is a multiple of 6 minutes and then starts the first thread
if (timeToExtract.minute%6!=0):
    time.sleep(60-timeToExtract.second + 60*(5-timeToExtract.minute%6))
print("Starting first thread")
collectData()
