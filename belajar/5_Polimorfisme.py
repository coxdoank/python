class Hewan:
    def __init__(self, nama):
        self.nama = nama
        
    def suara(self):
        pass
    
class Kucing(Hewan):
    def suara(self):
        print("Meow")
    
class Anjing(Hewan):
    def suara(self):
        print("Guk")

# Fungsi polimorfisme
def suara_hewan(hewan):
    hewan.suara()

# Membuat objek
kucing1 = Kucing("Kitty")
anjing1 = Anjing("Doge")

# Memanggil fungsi polimorfisme
suara_hewan(kucing1)
suara_hewan(anjing1)
