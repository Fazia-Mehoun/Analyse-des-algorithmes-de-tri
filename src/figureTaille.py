import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/resultatAlgo.csv', delimiter=',')

# Nettoyer les noms des colonnes en supprimant les espaces inutiles
df.columns = df.columns.str.strip()

print(df.dtypes)

# Conversion explicite des colonnes en types numériques
df['Taille'] = pd.to_numeric(df['Taille'], errors='coerce')
df['Temps d’execution'] = pd.to_numeric(df['Temps d’execution'], errors='coerce')
df['Comparaisons'] = pd.to_numeric(df['Comparaisons'], errors='coerce')
df['Accès mémoire'] = pd.to_numeric(df['Accès mémoire'], errors='coerce')

df = df.dropna()

print(df.head())  # Afficher les premières lignes pour vérifier les données

algorithms = df['Type Algo'].unique()
print(f"Algorithmes dans les données : {algorithms}")  # Afficher les algorithmes pour vérifier

# Premier graphique : Temps d'exécution en fonction de la Taille
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taille'])
    plt.plot(algo_data['Taille'].to_numpy(), algo_data['Temps d’execution'].to_numpy(), label=algo, marker='o')  # Tracer la courbe

plt.title("Temps d'Exécution en fonction de la Taille pour chaque Algorithme")
plt.xlabel('Taille')
plt.ylabel('Temps d\'exécution (en secondes)')
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()

# Deuxième graphique : Comparaisons en fonction de la Taille
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taille'])
    plt.plot(algo_data['Taille'].to_numpy(), algo_data['Comparaisons'].to_numpy(), label=algo, marker='o')

plt.title("Comparaisons en fonction de la Taille pour chaque Algorithme")
plt.xlabel('Taille')
plt.ylabel('Comparaisons')
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()

# Troisième graphique : Accès mémoire en fonction de la Taille
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taille'])
    plt.plot(algo_data['Taille'].to_numpy(), algo_data['Accès mémoire'].to_numpy(), label=algo, marker='o')

plt.title("Accès Mémoire en fonction de la Taille pour chaque Algorithme")
plt.xlabel('Taille')
plt.ylabel('Accès à la mémoire')
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()
