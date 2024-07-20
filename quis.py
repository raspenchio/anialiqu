import plotly.graph_objects as go

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3]), go.Scatter(x=[4, 5, 6])])
fig.update_layout(xaxis=dict(domain=[0, 0.5]))
fig.update_layout(xaxis2=dict(domain=[0.5, 1]))
