# JOINing data from multiple table - cleanup

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""SELECT DISTINCT population.city,
                  population.population, region.region
                  FROM population, region
                  WHERE population.city = region.city
                  ORDER by population.city ASC""")

    rows = c.fetchall()

    for r in rows:
        print "City: " + r[0]
        print "Population: " + str(r[1])
        print "Region: " + r[2]
        print
