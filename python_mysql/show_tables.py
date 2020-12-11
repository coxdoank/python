import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql",
    database = "datacamp"
)

cursor = db.cursor()

## getting all the tables which are present in 'datacamp' database
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)