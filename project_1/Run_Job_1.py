import subprocess
import os

# Mendapatkan path direktori saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Eksekusi file pertama
subprocess.call(["python", os.path.join(current_dir, "1_InsertDataToDB.py")])

# Eksekusi file kedua
subprocess.call(["python", os.path.join(current_dir, "2_ChangeFilename.py")])
