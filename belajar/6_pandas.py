import pandas as pd

# Membuat dataframe
data = {'Nama': ['John', 'Sarah', 'David', 'Anna'],
        'Usia': [25, 30, 35, 28],
        'Pekerjaan': ['Guru', 'Dokter', 'Insinyur', 'Pengacara']}
df = pd.DataFrame(data)

# Menampilkan dataframe
print(df)
