import numpy as np
import plotly.graph_objects as go

# Time range
t = np.linspace(0, 10, 400)

# Defining complex conjugate roots s_i = a + bi and s_i* = a - bi
a = -0.1  # Real part
b = 1.0  # Imaginary part

# Calculating e^{s_i t} and e^{s_i* t}
e_st = np.exp((a + 1j * b) * t)
e_s_conjugate_t = np.exp((a - 1j * b) * t)

# Create the plot
fig = go.Figure()

# Plot Re(e^{s_i t}) and Im(e^{s_i t})
fig.add_trace(go.Scatter(x=t, y=e_st.real, mode="lines", name="Re(e^{s_i t})"))
fig.add_trace(go.Scatter(x=t, y=e_st.imag, mode="lines", name="Im(e^{s_i t})"))

# Plot Re(e^{s_i* t}) and Im(e^{s_i* t})
fig.add_trace(
    go.Scatter(x=t, y=e_s_conjugate_t.real, mode="lines", name="Re(e^{s_i* t})")
)
fig.add_trace(
    go.Scatter(x=t, y=e_s_conjugate_t.imag, mode="lines", name="Im(e^{s_i* t})")
)

# Update layout for titles and axis labels
fig.update_layout(
    title="Visualization of $e^{s_i t}$ and $e^{s_i* t}$",
    xaxis_title="t",
    yaxis_title="Value",
    legend_title="Components",
)

# Show the plot
fig.show()

