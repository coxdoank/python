import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-G7RN3PM;'
                      'Database=pointofsales;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('''

SELECT 
[customerID] ,[name] ,[email] ,[phone_no] ,[address] ,[city] 
FROM [PointOfSales].[dbo].[customer]

''')

for row in cursor:
    print(row)