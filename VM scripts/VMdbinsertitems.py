#this program was run once to set up the items database with all the current items in the game

import mysql.connector
from datetime import datetime, timezone
import json
import requests

mydb = mysql.connector.connect(
    host = "Hack me if you can",
    user = 'root',
    password = "Please don't actually hack me",
    database = 'index')
myCursor = mydb.cursor() #cursor to interact with the database

timeToExtract = datetime.utcnow()
print (timeToExtract)
print (timeToExtract.timestamp()*1000) #timestamp to use with the rsbuddy api

URL = "https://rsbuddy.com/exchange/summary.json?ts=" + str(int(timeToExtract.timestamp()*1000))
data = requests.get(url = URL, params = {}).json() #query the rsbuddy api

vals = []
for item in data:
    vals.append((data[item]["id"],data[item]["name"],data[item]["members"]))
print(vals[0]) #debug
print(vals[150]) #debug

sql = "INSERT INTO items (id, name, members) VALUES (%s, %s, %s)"
myCursor.executemany(sql, vals) #this executes the sql command over every row in the vals array
mydb.commit()
print(myCursor.rowcount)
