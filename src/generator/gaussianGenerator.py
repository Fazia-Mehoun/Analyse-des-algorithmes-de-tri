import random
import numpy as np

"""
Classe pour générer des données suivant une distribution gaussienne et les retourner triées.
"""
class gaussianGenerator:
    def __init__(self, mean, std):
        self.mean = mean
        self.std = std

    def generate_data(self, size):
        data = np.random.normal(self.mean, self.std, size)
        data.sort()
        return data
