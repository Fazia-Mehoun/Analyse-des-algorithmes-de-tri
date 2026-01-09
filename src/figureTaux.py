import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/resultatAlgo.csv', delimiter=',')

df.columns = df.columns.str.strip()

df['Taille'] = 0  # Remplacez par la valeur 0
df['Shannon'] = 0  # Remplacez par la valeur 0

# Conversion explicite des colonnes en types numériques
df['Taux'] = pd.to_numeric(df['Taux'], errors='coerce')
df['Temps d’execution'] = pd.to_numeric(df['Temps d’execution'], errors='coerce')
df['Comparaisons'] = pd.to_numeric(df['Comparaisons'], errors='coerce')
df['Accès mémoire'] = pd.to_numeric(df['Accès mémoire'], errors='coerce')

df = df.dropna()

print(df.head())

algorithms = df['Type Algo'].unique()
print(f"Algorithmes dans les données : {algorithms}")

# Premier graphique : Temps d'exécution en fonction de la Taux
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taux'])
    plt.plot(algo_data['Taux'].to_numpy(), algo_data['Temps d’execution'].to_numpy(), label=algo, marker='o')

plt.title("Temps d'Exécution en fonction du taux de désordre pour chaque Algorithme")
plt.xlabel("Taux de désordre")
plt.ylabel("Temps d'exécution (en secondes)")
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()

# Deuxième graphique : Comparaisons en fonction de la Taux
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taux'])
    plt.plot(algo_data['Taux'].to_numpy(), algo_data['Comparaisons'].to_numpy(), label=algo, marker='o')

plt.title("Comparaisons en fonction du taux de désordre pour chaque Algorithme")
plt.xlabel("Taux de désordre")
plt.ylabel("Comparaisons")
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()

# Troisième graphique : Accès mémoire en fonction de la Taux
plt.figure(figsize=(10, 6))
for algo in algorithms:
    algo_data = df[df['Type Algo'] == algo].drop_duplicates(subset=['Taux'])
    plt.plot(algo_data['Taux'].to_numpy(), algo_data['Accès mémoire'].to_numpy(), label=algo, marker='o')

plt.title("Accès Mémoire en fonction du taux de désordre pour chaque Algorithme")
plt.xlabel("Taux de désordre")
plt.ylabel("Accès à la mémoire")
plt.legend(title="Algorithmes")
plt.tight_layout()
plt.show()
