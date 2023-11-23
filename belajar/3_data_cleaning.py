import pandas as pd

# Membuat dataframe
df = pd.DataFrame({'Nama': ['John', 'Sarah', 'David', 'Anna'],
                   'Usia': [25, None, 35, 28],
                   'Pekerjaan': ['Guru', 'Dokter', None, 'Pengacara']})

# Menampilkan data sebelum cleaning
print("Data Sebelum Cleaning:")
print(df)

# Membersihkan nilai kosong
df_clean = df.dropna()

# Menampilkan data setelah cleaning
print("Data Setelah Cleaning:")
print(df_clean)
