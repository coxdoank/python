class Manusia:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)

# Membuat objek
manusia1 = Manusia("John", 25)
manusia2 = Manusia("Doe", 30)

# Menampilkan informasi objek
manusia1.info()
manusia2.info()
