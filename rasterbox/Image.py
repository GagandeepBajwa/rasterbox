import numpy as np
from Utils.Misc import *
from Utils.DataManip import *

class Image(object):
    def __init__(self, bin):
        samples, lines, bands, data = read_binary(bin)
        self.samples, self.lines, self.bands = \
            int(samples), int(lines), int(bands)
        self.Data = data

    def ravel(self):
        return ravel(self.lines, self.samples, self.bands, self.Data)
    def spatial(self):
        return spatial(self.lines, self.samples, self.bands, self.Data)

    def __build_rgb(self):
        arr = np.zeros((self.lines, self.samples, 3))
        print("rgb shape:", arr.shape)

        for i in range(0, 3):
            arr[:, :, i] = self.Data[3 - i, :].reshape((self.lines, self.samples))

        for i in range(0, 3):
            arr[:, :, i] = rescale(arr[:, :, i])

        self.rgb = arr