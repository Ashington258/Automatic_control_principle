import numpy as np
import plotly.graph_objs as go

# 定义复指数函数
def exp_complex(s):
    return np.exp(s)

# 定义参数范围，实部和虚部的区间
real_values = np.linspace(-2, 2, 400)
imag_values = np.linspace(-2, 2, 400)

# 网格化实部和虚部，生成复数平面上的点
real_grid, imag_grid = np.meshgrid(real_values, imag_values)
s_values = real_grid + 1j * imag_grid

# 计算复指数函数的结果
exp_values = exp_complex(s_values)

# 分别提取实部和虚部
exp_real = np.real(exp_values)
exp_imag = np.imag(exp_values)

# 创建实平面和复平面的图形
fig = go.Figure()

# 绘制复指数函数实部在复数平面的图形
fig.add_trace(go.Surface(
    x=real_grid, y=imag_grid, z=exp_real, colorscale='Viridis',
    colorbar=dict(title="Real Part"),
    name='Real part'
))

# 绘制复指数函数虚部在复数平面的图形
fig.add_trace(go.Surface(
    x=real_grid, y=imag_grid, z=exp_imag, colorscale='Cividis',
    showscale=False, opacity=0.6,
    name='Imaginary part'
))

# 添加图形布局
fig.update_layout(
    title="Visualization of $e^s$ (Complex Exponential)",
    scene=dict(
        xaxis_title="Real part of s",
        yaxis_title="Imaginary part of s",
        zaxis_title="Value of $e^s$"
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

# 显示图形
fig.show()
