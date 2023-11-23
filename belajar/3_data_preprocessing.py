from sklearn.preprocessing import MinMaxScaler

# Membuat data
data = [[10, 20], [30, 40], [50, 60]]

# Scaling
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Menampilkan data setelah scaling
print("Data Setelah Scaling:")
print(data_scaled)
