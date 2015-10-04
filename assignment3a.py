# Database containing 100 random integers ranging from 0 to 100


# import the sql library
import sqlite3
import random

# create the database, if it doesn't already exist
conn = sqlite3.connect("newnum.db")

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    # delete database table if exist
    c.execute("DROP TABLE if exists numbers")

    # create database table
    c.execute("CREATE TABLE numbers(num int)")

    # insert each number to the database
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))

    c.execute("SELECT * FROM numbers")

    rows = c.fetchall()

    for r in rows:
        print r[0]
