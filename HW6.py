import psycopg2
from psycopg2 import sql

# connect to the db
conn = psycopg2.connect("dbname=431hw6 user=postgres")

# cursor
cur = conn.cursor()

cur.execute("CREATE SCHEMA IF NOT EXISTS EspanaC")
cur.execute("CREATE TABLE IF NOT EXISTS EspanaC.movie(title varchar, yr int);")

done = "n"
print("Populating movie Database")
while done != "y":
    movie = input("Enter movie title: ")
    year = input("Enter year of release: ")

    query = sql.SQL("INSERT INTO EspanaC.movie(title,yr) VALUES ({movieName}, {movieYear})").format(
        movieName=sql.Literal(movie),
        movieYear=sql.Literal(year)
    )
    cur.execute(query)
    conn.commit()
    done = input("Are you done? (y/n)")

# Shows database after new movies added
if done == "y":
    cur.execute("SELECT * from EspanaC.movie")
    rows = cur.fetchall()
    for row in rows:
        print("title: ", row[0])
        print("yr: ", row[1])
        print("\n")

    cur.close()
    quit()

# close the connection
conn.close()
