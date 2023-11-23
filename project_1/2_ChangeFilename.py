import os
import shutil
import datetime

# Mendefinisikan direktori file dan nama file yang akan diubah
file_path = "./sampledata/data_pemain_bola.csv"

# Menggunakan fungsi os.path.basename untuk mengambil nama file dari path
file_name = os.path.basename(file_path)

# Menggunakan os.path.splitext() untuk memisahkan nama file dan ekstensinya
# name, extension = os.path.splitext(file_name)
name, extension = os.path.splitext(file_name)

# Membuat objek datetime untuk mendapatkan tanggal dan waktu saat ini
now = datetime.datetime.now()

# Membuat format string untuk nama file baru
new_name = name + "_" + now.strftime("%Y-%m-%d_%H-%M-%S") + ".csv"

# Mengubah nama file dengan menggunakan fungsi os.rename
os.rename(file_path, new_name)

# Memindahkan file baru ke direktori tujuan dengan menggunakan shutil.move
destination_path = "./sampledata/"
shutil.move(new_name, destination_path)
