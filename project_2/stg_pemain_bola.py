from connection_db_mysql import create_db_connection

# Membuat koneksi
mydb = create_db_connection("localhost", "root", "", "tutorial")

# Membuat objek cursor
mycursor = mydb.cursor()

# Contoh query
query = "SELECT * FROM pemain_bola"

# Mengeksekusi query
mycursor.execute(query)

# Mengambil hasil query
results = mycursor.fetchall()

# Menampilkan data
for row in results:
    print(row)

# Menutup koneksi
mycursor.close()
mydb.close()