import matplotlib.pyplot as plt


def load_im(fname):
    source_im = plt.imread(fname)[:,:,:3] * 255
    source_im = source_im.astype(np.uint8)
    return source_im
