import numpy as np
import matplotlib.pyplot as plt
import control as ctrl


# 定义函数绘制根轨迹
def plot_root_locus(a):
    # 定义传递函数
    num = [1, 1]  # 对应 K(s + 1)
    den = [1, 0, a]  # 对应 s^2(s + a)
    system = ctrl.TransferFunction(num, den)

    # 计算根轨迹并绘制
    rlist, klist = ctrl.root_locus(system, plot=True)
    plt.title(f"根轨迹图 (a = {a})")
    plt.xlabel("实部")
    plt.ylabel("虚部")
    plt.grid()
    plt.show()


# 绘制不同 a 值的根轨迹
for a in [8, 9, 10]:
    plot_root_locus(a)
