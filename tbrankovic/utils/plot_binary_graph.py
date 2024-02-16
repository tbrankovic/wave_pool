import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

from tbrankovic.utils.convert_text_to_binary import convert_text_to_binary


def plot_binary_graph(stream, style='default'):
    fig = plt.figure(figsize=(6, 2), dpi=100)
    fig.patch.set_facecolor('#f1f1f9')

    ax = fig.add_subplot(111)
    ax.stem(stream, linefmt='black', markerfmt='.', basefmt=' ')
    ax.grid(True, color='white')
    ax.set_facecolor('#f1f1f9')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(-0.1, len(stream) + 0.1)
    ax.set_ylim(-0.1, 1.1)

    # Set y-ticks to [0, 1]
    ax.set_yticks([0, 1])
    # Set y-tick labels
    ax.set_yticklabels(['0', '1'])

    plt.grid(True, color='white')
    plt.show()

    return fig


# text = 'a'
# arr = convert_text_to_binary(text)
# plot_binary_graph(arr)
