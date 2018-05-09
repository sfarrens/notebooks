import numpy as np
import matplotlib.pyplot as plt


def regression_plot(x1, y1, x2, y2):

    plt.plot(x1, y1, 'o', color="#19C3F5", label='Data')
    plt.plot(x2, y2, '--', color='#FF4F5B', label='Model')
    plt.title('Best Fit Line', fontsize=20)
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.legend()
    plt.show()


def grad_plot(x, y1, y2, dy, point):

    plt.plot(x, y1, 'b-', label='$||x||_2$')
    plt.plot(x, y2, 'g-', label='$||x||_2^2$')
    plt.plot(x[point], y2[point], 'ro')
    plt.plot(x, dy, 'r--', label='Grad $||x_i||_2^2$')
    plt.ylim(-0.1, 1.0)
    plt.title('Convex L2-Norm')
    plt.xlabel('$x$', fontsize=24)
    plt.legend(loc='upper center', fontsize=20)
    plt.show()


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
    if not isinstance(xlab, type(None)):
        plt.xlabel(xlab, fontsize=18)
    if not isinstance(ylab, type(None)):
        plt.ylabel(ylab, fontsize=18)
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.show()


def line_plot(data, title=None, ylim=None):

    plt.plot(data, color='#F76F66')
    plt.plot(np.zeros(data.size), linestyle="--", color="grey")
    if not isinstance(title, type(None)):
        plt.title(title, fontsize=20)
    plt.ylim(ylim)
    plt.show()


def cost_plot(data):

    plt.plot(data, linestyle='-', color='#FF4F5B')
    plt.xlabel('Iteration', fontsize=18)
    plt.ylabel('Cost', fontsize=18)
    plt.title('Cost Function', fontsize=20)
    plt.show()


def display(data, title='example', shape=None, cmap='gist_stern', vmax=None,
            vmin=None):

    if not isinstance(shape, type(None)):
        data = data.reshape(shape)

    cax = plt.imshow(np.abs(data), cmap=cmap, vmin=vmin, vmax=vmax)
    plt.title(title, fontsize=20)
    plt.colorbar(cax)
    plt.show()
