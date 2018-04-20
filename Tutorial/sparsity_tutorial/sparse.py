import numpy as np


# Function to mask a signal.
def mask_op(signal, mask):

    return signal[np.where(mask == 1)[0]]


# Function to upsample a signal.
def upsample(signal, mask, dtype=complex):

    val = np.copy(mask).astype(dtype)
    val[val == 1] *= signal
    return val


# Function to measure the l1 norm.
def l1_norm(signal):

    return np.sum(np.abs(signal))


def soft_thresh(data, threshold):

    return np.around(np.maximum((1.0 - threshold / np.maximum(
                     np.finfo(np.float64).eps, np.abs(data))),
                             0.0) * data, decimals=15)
