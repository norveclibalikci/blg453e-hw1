import numpy as np


def calculate_hist(x):
    bins = [np.sum(x == b) for b in range(256)]
    return np.array(bins)


def calculate_cdf(bins):
    A = np.sum(bins)
    cdf = [np.sum(bins[:i]) for i in range(1, len(bins)+1)] / A
    return cdf


def construct_lut(x, y):
    LUT = np.zeros(256)
    g_j = 0
    for g_i in range(256):
        while x[g_j] < y[g_i] and g_j < 255:
            g_j += 1
        LUT[g_i] = g_j
    return LUT
