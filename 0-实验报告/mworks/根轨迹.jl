using ControlSystems
using TyPlot

# 定义绘制根轨迹的函数
function plot_root_locus(a)
    # 定义传递函数 G(s)
    num = [1, 1]      # 对应 K(s + 1)
    den = [1, 0, a]   # 对应 s^2(s + a)
    sys = tf(num, den)

    # 绘制根轨迹
    rlocus(sys)
    title!("根轨迹图 (a = $a)")
    xlabel!("实部")
    ylabel!("虚部")
    grid!(true)
end

# 绘制不同 a 值的根轨迹
for a in [8, 9, 10]
    plot_root_locus(a)
end
