import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the complex polynomial D(s) = s^4 + 2s^3 + 3s^2 + 4s + 5
def D_real(x, y):
    s = x + 1j * y
    D = s**4 + 2*s**3 + 3*s**2 + 4*s + 5
    return np.real(D)

def D_imag(x, y):
    s = x + 1j * y
    D = s**4 + 2*s**3 + 3*s**2 + 4*s + 5
    return np.imag(D)

# Create a grid of values for x and y
x_vals = np.linspace(-3, 3, 400)
y_vals = np.linspace(-3, 3, 400)
x, y = np.meshgrid(x_vals, y_vals)

# Calculate the real and imaginary parts of D(s) over the grid
D_real_vals = D_real(x, y)
D_imag_vals = D_imag(x, y)

# Plotting the real part of D(s)
fig = plt.figure(figsize=(14, 7))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, D_real_vals, cmap='viridis')
ax1.set_title('Real Part of D(s)')
ax1.set_xlabel('Re(s)')
ax1.set_ylabel('Im(s)')
ax1.set_zlabel('Re(D(s))')

# Plotting the imaginary part of D(s)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x, y, D_imag_vals, cmap='plasma')
ax2.set_title('Imaginary Part of D(s)')
ax2.set_xlabel('Re(s)')
ax2.set_ylabel('Im(s)')
ax2.set_zlabel('Im(D(s))')

plt.tight_layout()
plt.show()
