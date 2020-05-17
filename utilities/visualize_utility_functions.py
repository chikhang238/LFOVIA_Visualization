colors = ['cyan', 'orange', 'red', 'purple', 'green', 'blue', 'brown', 'olive']
import random
from matplotlib.gridspec import GridSpec
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go


def plot_twinx(ax, title, x_label, y_data1, y_label1, y_data2 , y_label2, color_1, color_2):
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label1, color = colors[color_1])

    ax.plot(y_data1, color = colors[color_1])

    ax_new = ax.twinx()
    ax_new.set_ylabel(y_label2, color = colors[color_2])
    ax_new.plot(y_data2, color = colors[color_2])

    return ax, ax_new


def plot_scatter_and_histogram_for_each_var(main_ax, x_hist, y_hist,  x_data, y_data, color = 'r'):

    main_ax.plot(x_data, y_data, 'ok', markersize=3, alpha=0.3, color = color)

    x_hist.hist(x_data, 40, histtype='stepfilled',
                orientation='vertical', color='gray')
    x_hist.invert_yaxis()

    y_hist.hist(y_data, 40, histtype='stepfilled',
                orientation='horizontal', color='gray')
    y_hist.invert_xaxis()
    return main_ax, x_hist, y_hist



def plot_trend_of_one_var(x_data, y_data):
    lr = LinearRegression()
    lr.fit(x_data.reshape(-1, 1), y_data.reshape(-1, 1))
    predicted_values = lr.predict(x_data.reshape(-1, 1))

    fig = go.Figure()
    fig.add_trace(go.Scatter(
                        x = x_data,
                        y = y_data, 
                        line_color = 'deepskyblue',
                        name = "original data",
        opacity = 0.8
    ))

    fig.add_trace(go.Scatter(
                    x = x_data,
                    y =  predicted_values.flatten(),
                    name = "Trend",
        line_color = 'red',
        opacity = 0.8

    ))

    return fig
