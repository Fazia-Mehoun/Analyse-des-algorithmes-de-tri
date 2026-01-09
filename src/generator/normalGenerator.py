import random
import numpy as np

"""
Classe pour générer des données suivant une distribution normale et les retourner triées.
"""
class normalGenerator:
    def __init__(self):
        pass
    def generate_data(self, size):
        data = [random.randint(0, size) for _ in range(size)]
        data.sort()
        return data
