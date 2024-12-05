import numpy as np
import matplotlib.pyplot as plt
from control import tf, root_locus

# Define the transfer function G(s) = K1(s + 1) / (s^2 * (s + 8))
numerator = [1, 1]  # Coefficients of (s + 1)
denominator = [1, 9, 0, 0]  # Coefficients of s^2 * (s + 8)
system = tf(numerator, denominator)

# Plot the root locus
plt.figure(figsize=(10, 6))
root_locus(system, grid=True)
plt.title("Root Locus of G(s) = K1(s + 1) / (s^2 * (s + 8))")
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.axhline(0, color='k', linestyle='--', linewidth=0.7)  # Real axis
plt.axvline(0, color='k', linestyle='--', linewidth=0.7)  # Imaginary axis
plt.show()
