import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# 定义复指数函数 e^s
def complex_exponential(s):
    return np.exp(s)


# 创建一个复数网格
def create_complex_grid(x_range, y_range, density=100):
    x = np.linspace(x_range[0], x_range[1], density)
    y = np.linspace(y_range[0], y_range[1], density)
    X, Y = np.meshgrid(x, y)
    S = X + 1j * Y
    return X, Y, S


# 计算 e^s 的实部、虚部和模
def compute_e_s(S):
    E_S = np.exp(S)
    E_S_real = np.real(E_S)
    E_S_imag = np.imag(E_S)
    E_S_mag = np.abs(E_S)
    E_S_phase = np.angle(E_S)
    return E_S_real, E_S_imag, E_S_mag, E_S_phase


# 创建复数网格
x_range = (-2, 2)
y_range = (-2 * np.pi, 2 * np.pi)
X, Y, S = create_complex_grid(x_range, y_range, density=200)

# 计算 e^s
E_S_real, E_S_imag, E_S_mag, E_S_phase = compute_e_s(S)

# 任务 2: 在实平面上的可视化（实部和虚部）
fig_real_plane = make_subplots(
    rows=1, cols=2, subplot_titles=("实部 Re(e^s)", "虚部 Im(e^s)")
)

# 绘制实部
fig_real_plane.add_trace(
    go.Contour(
        x=X[0],
        y=Y[:, 0],
        z=E_S_real,
        colorscale="Viridis",
        colorbar=dict(title="Re(e^s)"),
        contours=dict(showlines=False),
    ),
    row=1,
    col=1,
)

# 绘制虚部
fig_real_plane.add_trace(
    go.Contour(
        x=X[0],
        y=Y[:, 0],
        z=E_S_imag,
        colorscale="Viridis",
        colorbar=dict(title="Im(e^s)"),
        contours=dict(showlines=False),
    ),
    row=1,
    col=2,
)

fig_real_plane.update_layout(
    title_text="复指数函数 e^s 在实平面上的可视化", height=600, width=1200
)

# 任务 3: 在复数空间的可视化（3D）
fig_complex_space = go.Figure()

fig_complex_space.add_trace(
    go.Surface(
        x=X,
        y=Y,
        z=E_S_mag,
        colorscale="Viridis",
        colorbar=dict(title="|e^s|"),
        showscale=True,
    )
)

fig_complex_space.update_layout(
    title="复指数函数 e^s 在复数空间中的模 |e^s|",
    scene=dict(xaxis_title="实部 Re(s)", yaxis_title="虚部 Im(s)", zaxis_title="|e^s|"),
    height=700,
    width=900,
)

# 任务 4: 交互式更改 s 的实部和虚部
# 这里，我们使用滑块来动态更改 s 的值并观察 e^s 的变化

# 为简化展示，假设 s 是一个固定的复数，通过滑块调整其实部和虚部

from ipywidgets import interact, FloatSlider
import plotly.io as pio


# 定义绘制单个 e^s 的函数
def plot_single_e_s(Re_s=0.0, Im_s=0.0):
    s = Re_s + 1j * Im_s
    e_s = np.exp(s)
    magnitude = np.abs(e_s)
    phase = np.angle(e_s)

    fig = make_subplots(
        rows=1, cols=2, subplot_titles=("e^s 的模 |e^s|", "e^s 在复平面上的位置")
    )

    # 绘制模
    fig.add_trace(
        go.Indicator(
            mode="number",
            value=magnitude,
            title={"text": "模 |e^s|"},
            domain={"row": 0, "column": 0},
        ),
        row=1,
        col=1,
    )

    # 绘制复平面位置
    fig.add_trace(
        go.Scatter(
            x=[0, e_s.real],
            y=[0, e_s.imag],
            mode="lines+markers",
            marker=dict(size=[10, 12], color=["blue", "red"]),
            line=dict(width=2),
        ),
        row=1,
        col=2,
    )

    fig.update_layout(title=f"当 s = {s} 时，e^s 的可视化", height=500, width=900)

    fig.show()


# 如果在 Jupyter Notebook 环境中，使用 interact 来创建滑块
# 否则，可以创建一个静态图示例

# 检测是否在 Jupyter 环境
try:
    get_ipython
    in_jupyter = True
except NameError:
    in_jupyter = False

if in_jupyter:
    interact(
        plot_single_e_s,
        Re_s=FloatSlider(value=0.0, min=-2.0, max=2.0, step=0.1, description="Re(s)"),
        Im_s=FloatSlider(
            value=0.0, min=-2 * np.pi, max=2 * np.pi, step=0.1, description="Im(s)"
        ),
    )
else:
    print("交互式滑块仅在 Jupyter Notebook 环境中可用。")

# 展示所有图形
fig_real_plane.show()
fig_complex_space.show()
