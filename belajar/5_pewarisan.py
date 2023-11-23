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

# Membuat objek
kucing1 = Kucing("Kitty")
anjing1 = Anjing("Doge")

# Memanggil method suara pada objek
kucing1.suara()
anjing1.suara()
