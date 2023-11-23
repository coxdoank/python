import csv
# import mysql.connector
from connection_db_mysql import create_db_connection

# Koneksi ke MySQL
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="tutorial"
# )

mydb = create_db_connection("192.168.0.103", "root", "", "tutorial")

mycursor = mydb.cursor()

# membuka file csv
with open('../sampledata/data_pemain_bola.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader) # skip header row
    for row in reader:
        # cek apakah data sudah ada dalam tabel
        mycursor.execute("SELECT COUNT(*) FROM pemain_bola WHERE nama = %s", (row[0],))
        result = mycursor.fetchone()
        if result[0] > 0:
            # jika sudah ada, lakukan update data
            sql = "UPDATE pemain_bola SET usia = %s, posisi = %s, tim = %s, tinggi = %s, berat = %s, gol = %s, assist = %s WHERE nama = %s"
            val = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])
            mycursor.execute(sql, val)
        else:
            # jika belum ada, lakukan insert data
            sql = "INSERT INTO pemain_bola (nama, usia, posisi, tim, tinggi, berat, gol, assist) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            mycursor.execute(sql, val)

# commit perubahan ke database
mydb.commit()

# print(mycursor.rowcount, "baris berhasil diinsert/update.")