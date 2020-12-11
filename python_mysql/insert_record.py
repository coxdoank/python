import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database = "datacamp"
)

cursor = db.cursor()

## defining the Query
query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
## storing values in a variable
values = ("Harry", "coxdoank")

## executing the query with values
cursor.execute(query, values)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

print(cursor.rowcount, "record inserted")