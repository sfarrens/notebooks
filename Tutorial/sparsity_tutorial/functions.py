import numpy as np


def l1_norm(signal):

    return np.sum(np.abs(signal))


def sigma_mad(signal):

    return 1.4826 * np.median(np.abs(signal - np.median(signal)))
