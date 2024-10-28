import numpy as np
import matplotlib.pyplot as plt

# 定义 K 的范围
K = np.linspace(0, 10, 400)

# 计算 s1 和 s2
s1 = -2 + np.sqrt(4 - K)
s2 = -2 - np.sqrt(4 - K)

# 处理 K > 4 的情况
s1[K > 4] = np.nan  # 使 s1 在 K > 4 时为无效值
s2[K > 4] = -2 - np.sqrt(K[K > 4] - 4)  # 计算 s2 的虚数部分

# 绘制图形
plt.figure(figsize=(10, 6))
plt.plot(K, s1, label=r'$s_1 = -2 + \sqrt{4 - K}$', color='blue')
plt.plot(K, s2, label=r'$s_2 = -2 - \sqrt{4 - K}$', color='red')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(4, color='grey', lw=0.5, ls='--')
plt.xlim(0, 10)
plt.ylim(-10, 2)
plt.xlabel('K')
plt.ylabel('s')
plt.title('Roots s1 and s2 as a function of K')
plt.legend()
plt.grid()
plt.show()
