import os
import math
import yaml
import struct
import numpy as np
from rasterbox.utilities import Misc
from rasterbox.Image import Image
from rasterbox.Target import Target

class rasterbox(object):
    def __init__(self, src, images_path, targets_path, target_dict):
        self.src = src
        self.targets = target_dict
        self.__build(images_path, targets_path)

    def __build(self, images_path, targets_path):
        images_path = os.path.join(self.src, '%s' % images_path)
        targets_path = os.path.join(self.src, '%s' % targets_path)
        if images_path == None or targets_path == None:
            raise FileNotFoundError("Couldn't locate images path or targets path")
        image_bins = self.__build_binaries(images_path)
        target_bins = self.__build_binaries(targets_path)

        self.__build_images(image_bins)
        self.__build_targets(target_bins)


    def __build_images(self, bins):
        for idx, bin in enumerate(bins):
            if 'S2' in bin:
                self.S2 = Image(bins[idx])
            elif 'L8' in bin:
                self.L8 = Image(bins[idx])
            else:
                err("Do not recognize file ", bin)


    def __build_targets(self, bins):
        self.Target = dict()

        for _, bin in enumerate(bins):
            self.Target.update({
                target:Target(target, bin, self.targets)
                for target in self.targets if target in bin.lower()
            })


    def __build_binaries(self,path):
        try:
            for root, dirs, files in os.walk(path, topdown=False):
                bin_files = [
                    os.path.join(path, '%s' % file)
                    for file in files if '.hdr' not in file
                ]
                return bin_files
        except:
            err("Error building headers and binaries for %s" % path)
    def combine_satellites(self):
        return np.append(self.S2, self.L8, axis=1)
