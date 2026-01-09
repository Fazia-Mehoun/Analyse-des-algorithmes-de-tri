import random
import numpy as np

"""
Classe pour générer des données suivant une distribution exponentielle et les retourner triées.
"""
class exponentialGenerator:
    def __init__(self):
        pass
    def generate_data(self, size):
        data = np.random.exponential(1, size)
        data.sort()
        return data
