import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function G(s)
numerator = [8, 0.8]  # 8(s + 0.1)
denominator = np.polymul([1, 0], np.polymul([1, 1, 1], [1, 4, 25]))  # s(s^2 + s + 1)(s^2 + 4s + 25)

# Create the transfer function
system = signal.TransferFunction(numerator, denominator)

# Generate Bode plot
frequencies, magnitude, phase = signal.bode(system)

# Plot the Bode magnitude
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.semilogx(frequencies, magnitude)  # Magnitude plot
plt.title("Bode Plot of G(s)")
plt.ylabel("Magnitude (dB)")
plt.grid(which="both", linestyle="--", linewidth=0.5)

# Plot the Bode phase
plt.subplot(2, 1, 2)
plt.semilogx(frequencies, phase)  # Phase plot
plt.ylabel("Phase (degrees)")
plt.xlabel("Frequency (rad/s)")
plt.grid(which="both", linestyle="--", linewidth=0.5)

plt.tight_layout()
plt.show()
