# Assignment 3b - return aggregation from prompt


import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    average = ("SELECT avg(num) FROM  numbers")
    maximum = ("SELECT max(num) FROM numbers")
    minimum = ("SELECT min(num) FROM numbers")
    sum = ("SELECT sum(num) FROM numbers")

    while True:
        prompt = raw_input("Enter a command: ")
        if prompt == "AVG":
            c.execute(average)
            result = c.fetchone()
            print prompt + ":", result[0]
        elif prompt == "MAX":
            c.execute(maximum)
            result2 = c.fetchone()
            print prompt + ":", result2[0]
        elif prompt == "MIN":
            c.execute(minimum)
            result3 = c.fetchone()
            print prompt + ":", result3[0]
        elif prompt == "SUM":
            c.execute(sum)
            result4 = c.fetchone()
            print prompt + ":", result4[0]
        elif prompt == "quit":
            print "You have quit the program."
            break
        else:
            print "Please enter a command: AVG, MAX, MIN, SUM, or quit."





