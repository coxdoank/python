import seaborn as sns
import matplotlib.pyplot as plt

# Membuat data
tips = sns.load_dataset("tips")

# Membuat plot
sns.barplot(x="day", y="total_bill", data=tips)

# Menambahkan judul dan label sumbu
plt.title("Total Bill per Hari")
plt.xlabel("Hari")
plt.ylabel("Total Bill")

# Menampilkan plot
plt.show()
