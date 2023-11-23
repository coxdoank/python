import numpy as np

# Membuat matriks
A = np.array([[1, 2], [3, 4]])

# Determinan
det = np.linalg.det(A)
print("Determinan:", det)

# Invers
inv = np.linalg.inv(A)
print("Invers:", inv)

# Transpose
trans = np.transpose(A)
print("Transpose:", trans)
