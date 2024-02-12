from plotly import graph_objects as go
from plotly.subplots import make_subplots


def plot_spaghetti(cases, targets, proc, suscept, r, margins, titles):
    fig = make_subplots(rows=2, cols=2, shared_xaxes=True, vertical_spacing=0.05, horizontal_spacing=0.05, subplot_titles=titles)
    fig.add_traces(cases.plot().data, rows=1, cols=1)
    fig.add_trace(go.Scatter(x=targets.index, y=targets, mode="markers"), row=1, col=1)
    fig.add_traces(proc.plot().data, rows=2, cols=1)
    fig.add_traces(suscept.plot().data, rows=1, cols=2)
    fig.add_traces(r.plot().data, rows=2, cols=2)
    return fig.update_layout(margin=margins, height=600)


def get_plotly_area_from_df(df, columns, colour):
    x_vals = df.index.to_list() + df.index[::-1].to_list()
    y_vals = df[columns[0]].to_list() + df[columns[1]][::-1].to_list()
    return go.Scatter(x=x_vals, y=y_vals, line={"width": 0.0, "color": colour}, fill="toself")


def add_ci_patch_to_plot(fig, df, colour, row, col):
    x_vals = df.index.to_list() + df.index[::-1].to_list()
    fig.add_trace(get_plotly_area_from_df(df, columns=[0.05, 0.95], colour=colour), row=row, col=col)
    fig.add_trace(go.Scatter(x=x_vals, y=df[0.5], line={"color": colour}), row=row, col=col)


def plot_uncertainty_patches(cases, targets, proc, suscept, r, margins, titles, colours):
    fig = make_subplots(rows=2, cols=2, shared_xaxes=True, vertical_spacing=0.05, horizontal_spacing=0.05, subplot_titles=titles)
    fig.add_trace(go.Scatter(x=targets.index, y=targets, mode="markers"), row=1, col=1)
    add_ci_patch_to_plot(fig, cases, colours[0], 1, 1)
    add_ci_patch_to_plot(fig, suscept, colours[1], 1, 2)
    add_ci_patch_to_plot(fig, r, colours[2], 2, 1)
    add_ci_patch_to_plot(fig, proc, colours[3], 2, 2)
    return fig.update_layout(margin=margins, height=600, showlegend=False)
