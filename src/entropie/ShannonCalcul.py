import math
import numpy as np
import sys

# Fonction qui calcule l'entropie de Shannon 
def shannon_entropy(data):
    freq_dict = {}
    total = len(data)
    # Calcul des fréquences de chaque symbole dans la liste
    for num in data:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    entropy = 0
    for count in freq_dict.values():
        p = count / total
        # Application de la formule de l'entropie de Shannon : H(X) = -Σ p(x) * log2(p(x))
        entropy -= p * math.log2(p)
    return entropy

# Fonction qui Génère une liste de taille N avec K symboles et une entropie proche de H_target
def generate_list_shannon(N, K, H_target):
    
    probs = np.random.dirichlet(np.ones(K), size=1)[0]  # Génère une distribution aléatoire
    probs = sorted(probs, reverse=True)  # Trier pour réduire l'entropie

    # Boucle pour générer une distribution de probabilités qui produit une entropie proche de H_target
    while abs((-sum(p * np.log2(p) for p in probs if p > 0)) - H_target) > 0.01:
        probs = np.random.dirichlet(np.ones(K), size=1)[0]  # Nouvelle distribution

    symboles = list(range(1, K+1)) 
    data = np.random.choice(symboles, size=N, p=probs)
    
    return list(data), shannon_entropy(data)



