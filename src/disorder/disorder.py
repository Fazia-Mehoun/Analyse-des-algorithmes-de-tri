import random

class disorder:
    def __init__(self):
        pass

    #Methode qui permert d'appliquer un taux de desordre sur nos données
    def apply_disorder(self, data, disorder_level):
        size = len(data)
        num_swaps = int(disorder_level * size // 2) 
        tab = list(range(size))  # Liste des indices disponibles
        for _ in range(num_swaps):
            if len(tab) < 2:  
                break
            i, j = random.sample(tab, 2)  # Choisir deux indices uniques
            data[i], data[j] = data[j], data[i]
            # Supprimer les indices déjà utilisés
            tab.remove(i)
            tab.remove(j)
        return data

    #Methode qui permet d'appliquer un taux de desordre à la fin de nos données
    def apply_disorder_last(self, data, nb_elements):
        size = len(data)
        if nb_elements > size:
            raise ValueError("Le nombre d'éléments à désordonner dépasse la taille de la liste.")  
        # Indices des éléments à désordonner (les derniers éléments)
        start_index = size - nb_elements
        sub_data = data[start_index:]
        # Désordonne uniquement la partie sélectionnée
        self.apply_disorder(sub_data, 1)
        # Replace la partie désordonnée dans la liste originale
        data[start_index:] = sub_data
        return data

    def apply_block_sorted(self, data, num_blocks):
        # Calcul de la taille des blocs
        block_size = len(data) // num_blocks
        remainder = len(data) % num_blocks
        # Divise les données en blocs avec un ajustement pour le reste
        blocks = []
        start = 0
        for i in range(num_blocks):
            end = start + block_size + (1 if i < remainder else 0)  # Distribue uniformément le reste
            blocks.append(data[start:end])
            start = end
        # Trie chaque bloc individuellement
        sorted_blocks = [sorted(block) for block in blocks]
        # Mélange les blocs triés
        random.shuffle(sorted_blocks)
        # Recompose la liste en concaténant les blocs
        result = [item for block in sorted_blocks for item in block]
        return result

    #Methode qui permet d'inverser les données (Triés inversement)
    def apply_inverse_sorted(self, data):
        return sorted(data, reverse=True)
