
import matplotlib.pyplot as plt

#Fonction permettant d'afficher les données dans un graphique à barres
def visualize_data_bar(data, title="Graphique des données"):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(data)), data, color='skyblue', edgecolor='skyblue')
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Valeur")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
