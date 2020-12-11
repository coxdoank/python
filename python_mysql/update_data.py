import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database = "datacamp"
)

cursor = db.cursor()

## defining the Query
query = "UPDATE users SET name = 'Kareem' WHERE id = 1"

## executing the query
cursor.execute(query)

## final step to tell the database that we have changed the table data
db.commit()