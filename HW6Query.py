import psycopg2
from psycopg2 import sql

# connect to the db
conn = psycopg2.connect("dbname=431hw6 user=postgres")

# cursor
cur = conn.cursor()

print("Searching for movies by title or by year")

titleSearch = "n"

done = "n"

while done != "y":
    titleSearch = input("Search for title? (y/n) ")
    if titleSearch == "y":
        titleName = input("Enter movie title: ")
        query = sql.SQL("SELECT * FROM EspanaC.movie WHERE {column} = {movieName}").format(
            column=sql.Identifier('title'),
            movieName=sql.Literal(titleName)
        )
        count = sql.SQL("SELECT COUNT ({column}) FROM EspanaC.movie").format(
            column=sql.Identifier('title')
        )

        cur.execute(query)

        rows = cur.fetchall()

        # if the database has the movie
        if rows:
            for row in rows:
                print("title: ", row[0])
                print("yr: ", row[1])
                print("\n")

            cur.execute(count)
            count = cur.fetchone()
            print("Number of movies in Database: ", count[0])

        else:
            print("Movie is not in Database")

        done = input("Are you done? ")

    # if prefer to search by year of movie released
    else:
        yearSearch = input("Enter year of release: ")
        query = sql.SQL("SELECT * FROM EspanaC.movie WHERE {column} = {movieYear}").format(
            column=sql.Identifier('yr'),
            movieYear=sql.Literal(yearSearch)
        )
        count = sql.SQL("SELECT COUNT ({column}) FROM EspanaC.movie").format(
            column=sql.Identifier('title')
        )

        cur.execute(query)
        rows = cur.fetchall()

        # if database has the movie
        if rows:
            for row in rows:
                print("title: ", row[0])
                print("yr: ", row[1])
                print("\n")

            cur.execute(count)
            count = cur.fetchone()
            print("Number of movies in Database: ", count[0])

        else:
            print("Movie is not in Database")

        done = input("Are you done? ")

# close the connection
conn.close()
