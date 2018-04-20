import numpy as np
import matplotlib.pyplot as plt


def stem_plot(data, title=None, imag=False):

    x_vals = np.arange(data.size)

    (markers, stemlines, baseline) = plt.stem(x_vals, np.real(data),
                                              label='Real')
    plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
    plt.setp(markers, marker='o', color="#19C3F5")
    plt.setp(baseline, linestyle="--", color="grey", linewidth=2)

    if imag:

        (markers, stemlines, baseline) = plt.stem(x_vals, np.imag(data),
                                                  label='Imaginary')
        plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
        plt.setp(markers, marker='o', color="#EA8663")
        plt.setp(baseline, linestyle="--", color="grey", linewidth=2)
        plt.legend(loc=1)

    plt.xlim(0, data.size)
    plt.ylim(-1, 2.5)
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.show()


def display(data, title='example', shape=None, cmap='gist_stern'):

    if not isinstance(shape, type(None)):
        data = data.reshape(shape)

    plt.imshow(np.abs(data), cmap=cmap)
    plt.title(title, fontsize=20)
    plt.colorbar()
    plt.show()
