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

def save_data(data, filename):
    with open(filename, "w") as file:
        for value in data:
            file.write(str(value) + "\n")

def write_log(distribution_choice, size, disorder_type, entropy):
    with open("../log/log.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if(distribution_choice == "-n"):
            distribution = "Normale"
        elif(distribution_choice == "-u"):
            distribution= "Uniforme"
        elif(distribution_choice == "-g"):
            distribution= "Gaussienne"
        elif(distribution_choice == "-e"):
            distribution = "Exponentielle"
        elif(distribution_choice == "shannon"):
            distribution = "Shannon"
        writer.writerow([distribution, size, disorder_type, entropy])


def print_help():
    help_text = """
    Utilisation : python3 main2.py <taille> <-n|-u|-g|-e> <type_désordre> [paramètres...]
    
    Arguments :
      <taille> : Nombre d'éléments à générer
      <-n|-u|-g|-e> : Type de distribution
         -n : Normale
         -u : Uniforme (nécessite <min> et <max>)
         -g : Gaussienne (nécessite <moyenne> et <variance>)
         -e : Exponentielle
      <type_désordre> : Type de désordre à appliquer
         taux <valeur> : Applique un désordre aléatoire avec un taux entre 0 et 1
         derniers <nombre> : Désordonne les <nombre> derniers éléments
         blocs <nombre> : Désordonne en <nombre> blocs triés
         inverse : Inverse complètement les données

      Mode Shannon :
         shannon <N> <K> <H_target> : Génère une liste de taille N avec K symboles et une entropie Shannon proche de H_target.

    Exemples :
      python3 generer.py 2000 -n taux 0.5
      python3 generer.py 5000 -u derniers 500 10 100
      python3 generer.py 3000 -g blocs 4 50 5
      python3 generer.py 1000 -e inverse
      python3 generer.py shannon 200 3 1.2
    """
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main2.py help pour voir les commandes disponibles.")
        sys.exit(1)
    
    if sys.argv[1].lower() in ["--help", "-h", "?"]:
        print_help()
        sys.exit(0)

    if len(sys.argv) > 1 and sys.argv[1] == "effacer":
        effacer()
        print("Le fichier a été nettoyé en conservant uniquement l'en-tête.")
    

    if sys.argv[1].lower() == "shannon":
        if len(sys.argv) != 5:
            print("Usage: python3 main.py shannon <N> <K> <H_target>")
            sys.exit(1)

        N = int(sys.argv[2])
        K = int(sys.argv[3])
        H_target = float(sys.argv[4])

        dis_data, computed_entropy = generate_list_shannon(N, K, H_target)
        
        save_data(dis_data, "../data/dis_data.csv")
        write_log("shannon", N, "Null", H_target)

        print(f"Entropie obtenue : {computed_entropy:.4f}")
        print("Extrait de la liste :", dis_data[:10])  
        visualize_data_bar(dis_data)
        sys.exit(0)

    if len(sys.argv) < 4:
        print("Usage: generer <taille> <-n|-u|-g|-e> <type_désordre> [paramètres...]")
        sys.exit(1)

    size = int(sys.argv[1])
    distribution_type = sys.argv[2].lower()
    disorder_type = sys.argv[3].lower()
    
    # Génération des données
    if distribution_type == "-n":
        generator = normalGenerator()
        data = generator.generate_data(size)
    elif distribution_type == "-u":
        if len(sys.argv) < 6:
            print("Usage: generer <taille> -u <type_désordre> <min> <max>")
            sys.exit(1)
        if disorder_type == "taux":
            min_val = int(sys.argv[5])
            max_val = int(sys.argv[6])
        else:
            min_val = int(sys.argv[4])
            max_val = int(sys.argv[5])
        generator = uniformGenerator(min_val, max_val)
        data = generator.generate_data(size)
    elif distribution_type == "-g":
        if len(sys.argv) < 6:
            print("Usage: generer <taille> -g <type_désordre> <moyenne> <variance>")
            sys.exit(1)
        mean = float(sys.argv[4])
        std = float(sys.argv[5])
        generator = gaussianGenerator(mean, std)
        data = generator.generate_data(size)
    elif distribution_type == "-e":
        generator = exponentialGenerator()
        data = generator.generate_data(size)
    else:
        print("Distribution invalide !")
        sys.exit(1)

    save_data(data, "../data/data.csv")
    dis = disorder()

    # Application du désordre
    if disorder_type == "taux":
        if len(sys.argv) < 5:
            print("Usage: generer <taille> <distribution> taux <valeur>")
            sys.exit(1)
        disorder_level = float(sys.argv[4])
        dis_data = dis.apply_disorder(data, disorder_level)
    elif disorder_type == "derniers":
        nb_elements = int(sys.argv[4])
        dis_data = dis.apply_disorder_last(data, nb_elements)
    elif disorder_type == "blocs":
        num_blocks = int(sys.argv[4])
        dis_data = dis.apply_block_sorted(data, num_blocks)
    elif disorder_type == "inverse":
        dis_data = dis.apply_inverse_sorted(data)
    else:
        print("Type de désordre invalide !")
        sys.exit(1)

    save_data(dis_data, "../data/dis_data.csv")
    write_log(distribution_type, size, disorder_type, 0)

    visualize_data_bar(dis_data)

if __name__ == "__main__":
    main()
