import matplotlib.pyplot as plt


def plot_graph(x, y, style='default'):
    fig = plt.figure(figsize=(6, 2), dpi=100)
    fig.patch.set_facecolor('#f1f1f9')

    ax = fig.add_subplot(111)
    ax.plot(x, y, color='black', linestyle='-', marker='.', markersize=0.7)
    ax.grid(True, color='white')
    ax.set_facecolor('#f1f1f9')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(True, color='white')
    plt.show()

    return fig
