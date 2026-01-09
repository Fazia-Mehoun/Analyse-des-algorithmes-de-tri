import random
import numpy as np

"""
Classe pour générer des données suivant une distribution uniforme et les retourner triées.
"""
class uniformGenerator:
    def __init__(self, min, max):
        self.min = min
        self.max = max
    
    def generate_data(self, size):
        data = np.random.uniform(self.min, self.max, size)
        data.sort()
        return data
