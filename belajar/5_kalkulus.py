import numpy as np
from scipy import integrate, misc

# Definisi fungsi
def f(x):
    return x ** 2

# Turunan
turunan = misc.derivative(f, 1.0)
print("Turunan:", turunan)

# Integral
integral, error = integrate.quad(f, 0, 2)
print("Integral:", integral)
print("Error:", error)
