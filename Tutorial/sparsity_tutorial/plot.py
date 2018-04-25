import numpy as np
import matplotlib.pyplot as plt


def stem_plot(data, x_vals=None, title=None, imag=True, ylim=None, xlab=None,
              ylab=None, line=False, f=None):

    if x_vals is None:
        x_vals = np.arange(data.size)

    if ylim is None:
        ylim = (-1, 2.5)

    (markers, stemlines, baseline) = plt.stem(x_vals, np.real(data),
                                              label='Real')
    plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
    plt.setp(markers, marker='o', color="#19C3F5")
    plt.setp(baseline, linestyle="--", color="grey", linewidth=2)
    if line:
        plt.plot(x_vals, data, linestyle="-", color='#FF4F5B')
    if f is not None:
        xx = np.arange(0, 1, 1/1000.)
        plt.plot(xx, np.sin(2 * np.pi * f * xx), 'g:')

    if imag:

        (markers, stemlines, baseline) = plt.stem(x_vals, np.imag(data),
                                                  label='Imaginary')
        plt.setp(stemlines, linestyle="-", color="grey", linewidth=0.5)
        plt.setp(markers, marker='o', color="#EA8663")
        plt.setp(baseline, linestyle="--", color="grey", linewidth=2)
        plt.legend(loc=1)

    plt.ylim(ylim)
    plt.xlabel(xlab, fontsize=18)
    plt.ylabel(ylab, fontsize=18)
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.show()


def line_plot(data, title=None):

    plt.plot(data, color='#F76F66')
    plt.plot(np.zeros(data.size), linestyle="--", color="grey")
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.show()


def cost_plot(data):

    plt.plot(data, linestyle='-', color='#FF4F5B')
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('Cost', fontsize=18)
    plt.title('Cost Function', fontsize=20)
    plt.show()


def display(data, title='example', shape=None, cmap='gist_stern'):

    if not isinstance(shape, type(None)):
        data = data.reshape(shape)

    plt.imshow(np.abs(data), cmap=cmap)
    plt.title(title, fontsize=20)
    plt.colorbar()
    plt.show()
