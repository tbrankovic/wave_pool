import matplotlib.pyplot as plt


def plot_waveform(x, y):
    fig = plt.figure(figsize=(13, 1), dpi=100)
    fig.patch.set_facecolor('#f1f1f9')

    ax = fig.add_subplot(111)
    ax.plot(x, y, color='black', linestyle='-')
    ax.grid(True, color='white')
    ax.set_facecolor('#f1f1f9')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.grid(True, color='white')
    plt.show()

    return fig