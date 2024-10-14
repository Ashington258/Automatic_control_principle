import numpy as np
import matplotlib.pyplot as plt

# 定义多项式系数
coefficients = [1, 2, 3, 4, 5]

# 计算根
roots = np.roots(coefficients)

# 绘制根的分布
plt.figure(figsize=(8, 8))
plt.scatter(roots.real, roots.imag, color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title('Roots of the Polynomial in the Complex Plane')
plt.xlabel('Real Part')
plt.ylabel('Imaginary Part')
plt.grid()
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.show()

# 输出根
print("Roots:", roots)

