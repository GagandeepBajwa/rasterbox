import numpy as np
import  matplotlib.pyplot as plt
from rasterbox.utilities import Misc
from rasterbox.utilities import DataManip


class Image(object):
    def __init__(self, bin):
        samples, lines, bands, data = Misc.read_binary(bin)
        self.samples, self.lines, self.bands = \
            int(samples), int(lines), int(bands)
        self.Data = data.reshape(self.bands, self.lines * self.samples)
        self.__build_rgb()


    def __build_rgb(self):
        arr = np.zeros((self.lines, self.samples, 3))

        for i in range(0, 3):
            arr[:, :, i] = self.Data[3 - i, :].reshape((self.lines, self.samples))

        for i in range(0, 3):
            arr[:, :, i] = DataManip.rescale(arr[:, :, i])

        self.rgb = arr


    def ravel(self):
        return ravel(self.lines, self.samples, self.bands, self.Data)


    def spatial(self):
        return spatial(self.lines, self.samples, self.bands, self.Data)


    def showplot(self):
        plt.imshow(self.rgb)
        plt.tight_layout()
        plt.show()