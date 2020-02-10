from rasterbox.utilities import Misc
import matplotlib.pyplot as plt
class Target(object):


    def __init__(self, name, bin, target_list):
        self.name = name
        s,l,b,self.Data = Misc.read_binary(bin)
        self.samples, self.lines, self.bands = int(s), int(l), int(b)
        self.__build_binary(target_list)


    def __build_binary(self, target_list):
        targets = target_list
        if self.name in targets:
            b = targets[self.name]['bool']
            val =  targets[self.name]['val']

            if b:
                self.Binary = self.Data == float(val)
            elif not b:
                self.Binary = self.Data != float(val)
            else:
                raise Exception('There was an error encoding binaries')


    def ravel(self, binary=True):
        if binary:
            return self.Binary.reshape(self.lines * self.samples)
        else:
            return self.Data.reshape(self.lines *  self.samples)


    def spatial(self, binary=True):
        if binary:
            return self.Binary.reshape(self.lines, self.samples)
        else:
            return self.Data.reshape(self.lines, self.samples)


    def showplot(self, binary=True):
        y = self.spatial(binary=binary)
        if binary:
            plt.imshow(y, cmap='gray')
        else:
            plt.imshow(y)
        plt.tight_layout()
        plt.show()