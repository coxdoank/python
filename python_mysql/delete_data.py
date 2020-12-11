import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database = "datacamp"
)

cursor = db.cursor()

## defining the Query
query = "DELETE FROM users WHERE id = 5"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()