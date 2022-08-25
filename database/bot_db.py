import sqlite3
from config import bot



def sql_create():
    global db , cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db :
        print("База данных подключена!")

    db.execute("CREATE TABLE IS NOT EXISTS anketa"
               " (id INTEGER PRYMARY KEY , username TEXT)"
               "photo TEXT , name TEXT, age TEXT,gender TEXT,region TEXT ")
    db.commit()
