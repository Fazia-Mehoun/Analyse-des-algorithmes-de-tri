import sys
import csv
import math
import numpy as np
from generator.normalGenerator import normalGenerator
from generator.uniformGenerator import uniformGenerator
from generator.gaussianGenerator import gaussianGenerator
from generator.exponentialGenerator import exponentialGenerator
from disorder.disorder import disorder
from chart.displayData import visualize_data_bar
from algotri.algorithms import algorithms   
from entropie.ShannonCalcul import *

sys.setrecursionlimit(100000)  

"""
    Sauvegarde les résultats d'un algorithme dans deux fichiers CSV.

    Cette fonction enregistre les résultats d'un algorithme de tri dans deux fichiers CSV. Le premier fichier, 
    `resultatAlgo.csv`, contient toutes les informations relatives à l'algorithme pour faire les analyses et les graphes, tandis que le deuxième, 
    `histo.csv`, enregistre les mêmes informations pour l'historique.

"""
def save_results(algo_name, size, distribution_type, disorder_type, tauxWrite , ShannonWrite , comparisons, memory_access, exec_time):
    """ Sauvegarde les résultats dans un fichier CSV """
    with open("../data/resultatAlgo.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([algo_name, size, distribution_type, disorder_type, tauxWrite , ShannonWrite , comparisons, memory_access, exec_time ])
        separateur = "============="
        writer.writerow([separateur, separateur, separateur, separateur, separateur, separateur, separateur])

    with open("../data/histo.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([algo_name, size, distribution_type, disorder_type, tauxWrite , ShannonWrite , comparisons, memory_access, exec_time ])
        separateur = "============="
        writer.writerow([separateur, separateur, separateur, separateur, separateur, separateur, separateur])


"""
    Efface toutes les lignes d'un fichier CSV, sauf l'en-tête.
"""
def effacer():
    input_file = "../data/resultatAlgo.csv"
    
    # Lire la première ligne (en-tête) du fichier
    with open(input_file, "r") as file:
        lines = file.readlines()
    
    # Écraser le fichier en gardant uniquement la première ligne
    with open(input_file, "w", newline="") as file:
        file.write(lines[0])  # Écrit l'en-tête


def main():

    if sys.argv[1].lower() in ["--help", "-h", "?"]:
        print_help()
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == "effacer":
        effacer()
        print("Le fichier a été nettoyé en conservant uniquement l'en-tête.")

    if len(sys.argv) < 5:
        print("Usage: python3 experimentation.py analyse <algo|tout> <taille> <-n|-u|-g|-e|-shannon> <type_désordre> [paramètres...]")
        sys.exit(1)
    
    mode = sys.argv[1].lower()
    
    if mode == "analyse":
        algo_input = sys.argv[2].lower()
        size = int(sys.argv[3])
        distribution_type = sys.argv[4].lower()
        disorder_type = sys.argv[5].lower()
        
        # Liste des algorithmes disponibles
        algorithm_list = ["bubble", "heap", "bucket" , "merge" , "selection"]
        
        if algo_input == "tout":
            algorithms_to_run = algorithm_list
        else:
            algorithms_to_run = [algo_input]

        print("\n===== Analyse de Tri =====")
        print(f" Taille des données     : {size}")
        print(f" Type de distribution   : {distribution_type}")
        print(f" Type de désordre       : {disorder_type}\n")

        # Génération des données
        if distribution_type == "-n":
            print(" Distribution : Normale")
            generator = normalGenerator()
            data = generator.generate_data(size)
        elif distribution_type == "-u":
            print(" Distribution : Uniforme")
            min_val, max_val = int(sys.argv[6]), int(sys.argv[7])
            generator = uniformGenerator(min_val, max_val)
            data = generator.generate_data(size)
        elif distribution_type == "-g":
            print(" Distribution : Gaussienne")
            mean, std = float(sys.argv[6]), float(sys.argv[7])
            generator = gaussianGenerator(mean, std)
            data = generator.generate_data(size)
        elif distribution_type == "-e":
            print(" Distribution : Exponentielle")
            generator = exponentialGenerator()
            data = generator.generate_data(size)
        elif distribution_type == "shannon":
            if len(sys.argv) < 7:
                print(" Erreur: paramètres insuffisants pour la distribution 'shannon'.")
                sys.exit(1)
            print(" Distribution : Shannon")
            N = size
            K = int(sys.argv[5])
            H_target = float(sys.argv[6])

            dis_data, computed_entropy = generate_list_shannon(N, K, H_target)
            
            print(f"✔ Entropie obtenue : {computed_entropy:.4f}")
            print(f"🔹 Extrait des données générées : {dis_data[:10]}")
        else:
            print("Distribution invalide !")
            sys.exit(1)

        dis = disorder()  
        

        # Application du désordre
        if distribution_type != "shannon":  # Shannon est déjà désordonné
            if disorder_type == "taux":
                disorder_level = float(sys.argv[6])
                dis_data = dis.apply_disorder(data, disorder_level)
                tauxWrite = disorder_level
                ShannonWrite = "Non important"
            elif disorder_type == "derniers":
                nb_elements = int(sys.argv[6])
                dis_data = dis.apply_disorder_last(data, nb_elements)
            elif disorder_type == "blocs":
                num_blocks = int(sys.argv[6])
                dis_data = dis.apply_block_sorted(data, num_blocks)
            elif disorder_type == "inverse":
                dis_data = dis.apply_inverse_sorted(data)
            else:
                print(" Type de désordre invalide !")
                sys.exit(1)
        else :
            tauxWrite = "Non important"
            ShannonWrite = H_target

        # Exécution des tris
        algo_instance = algorithms()

        for algo_name in algorithms_to_run:
            algo_method = algo_name + "_sort"
            if not hasattr(algo_instance, algo_method):
                print(f"⚠ Algorithme {algo_name} non trouvé.")
                continue

            print(f"\n--- Exécution du tri : {algo_name.capitalize()} ---")
            sorted_data, comparisons, memory_access, exec_time = getattr(algo_instance, algo_method)(dis_data)


            # Sauvegarde des résultats
            save_results(algo_name.capitalize(), size, distribution_type, disorder_type, tauxWrite , ShannonWrite ,comparisons, memory_access, exec_time)

            print(f"✔ Tri {algo_name.capitalize()} terminé en {exec_time:.4f} secondes.")
            print(f"   Comparaisons      : {comparisons}")
            print(f"   Accès mémoire     : {memory_access}")

        sys.exit(0)
    else:
        print(" Commande invalide. Utilisez 'analyse' pour exécuter un tri.")
        sys.exit(1)

if __name__ == "__main__":
    main()


"""

for valeur in 100 200 300 400 500 600 700 800 900 1000 2000 3000 4000 5000 6000 7000 8000 9000 10000 15000 ; do
    python3 experimentation.py analyse tout $valeur -n taux 0.5
done


for taux in $(seq 0.05 0.05 1.0 | sed 's/,/./g'); do
    python3 experimentation.py analyse tout 1000 -n taux $taux
done


for val in 0.1 0.3 0.5 0.7 0.9 1 1.2 1.4 1.5 1.7 1.9 ; do
    python3 experimentation.py analyse tout 1000 shannon 4 $val
done

"""
