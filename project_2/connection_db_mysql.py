import mysql.connector

def create_db_connection(host, user, password, database):
    """
    Fungsi untuk membuat koneksi ke MySQL.
    Mengembalikan objek koneksi jika berhasil, atau None jika gagal.
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return conn
        # if conn.is_connected():
        #     print("Berhasil terkoneksi ke database MySQL.")
        #     return conn
    except mysql.connector.Error as e:
        print("Error dalam mengkoneksikan ke database MySQL: ", e)