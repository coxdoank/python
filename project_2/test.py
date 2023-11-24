import mysql.connector

def connect_to_mysql(host, user, password, database):
    try:
        # Konfigurasi koneksi MySQL
        db_config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
        }

        # Membuat koneksi
        conn = mysql.connector.connect(**db_config)

        # Mengembalikan objek koneksi
        return conn

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Gantilah dengan informasi koneksi MySQL Anda
host = 'localhost'
user = 'root'
password = ''
database = 'tutorial'

# Memanggil fungsi koneksi
connection = connect_to_mysql(host, user, password, database)

if connection:
    print("Koneksi berhasil!")

    try:
        # Membuat objek cursor
        cursor = connection.cursor()

        # Contoh query untuk memindahkan data dari 'pemain_bola' ke 'pemain_bola_indonesia'
        select_query = "SELECT * FROM pemain_bola"
        insert_query = "INSERT INTO pemain_bola_indonesia (nama, tim) VALUES (%s, %s)"

        # Eksekusi query untuk membaca data dari 'pemain_bola'
        cursor.execute(select_query)

        # Mendapatkan semua baris hasil query
        results = cursor.fetchall()

        # Menghitung jumlah data untuk menampilkan progres
        total_data = len(results)
        progress = 0

        # Iterasi untuk memindahkan data satu per satu
        for entry in results:
            cursor.execute(insert_query, entry)
            connection.commit()

            # Menampilkan progres
            progress += 1
            print(f"Progres: {progress}/{total_data}")

        # Menutup cursor
        cursor.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Jangan lupa menutup koneksi setelah selesai
    connection.close()
    print("Koneksi ditutup.")
