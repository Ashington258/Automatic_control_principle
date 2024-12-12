import numpy as np
import matplotlib.pyplot as plt


# 定义方程的系数
def polynomial_coefficients(K1, a):
    # 系数为s^2(s + a) + K1(s + 1) = 0
    # 展开得到：s^3 + as^2 + K1*s + K1 = 0
    return [1, a, K1, K1]


# 设置参数
K1_values = np.linspace(0, 100, 5000)  # K1 从 0 到 100
a_values = [8, 9, 10]
colors = ["blue", "orange", "green"]  # 不同颜色

# 为每个 a 值创建单独的图形
for a, color in zip(a_values, colors):
    plt.figure(figsize=(10, 8))
    roots_real = []
    roots_imag = []

    for K1 in K1_values:
        coeffs = polynomial_coefficients(K1, a)  # 获取系数
        r = np.roots(coeffs)  # 计算根
        roots_real.extend(r.real)  # 添加实部
        roots_imag.extend(r.imag)  # 添加虚部

    # 绘制根分布，设置点的大小
    plt.scatter(
        roots_real, roots_imag, color=color, alpha=0.5, s=10
    )  # s=10 设置点的大小

    # 设置图形属性
    plt.axhline(0, color="black", lw=0.5, ls="--")
    plt.axvline(0, color="black", lw=0.5, ls="--")
    plt.title(f"Root Distribution in the Complex Plane (a = {a})")
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    plt.grid()
    plt.show()
