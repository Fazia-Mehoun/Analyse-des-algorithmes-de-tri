
#  Étude des Performances des Algorithmes de Tri

Un projet en **Python** permettant d’analyser et de comparer les performances de plusieurs **algorithmes de tri**
en fonction de différents paramètres : **taille des données**, **niveau de désordre**, **distribution statistique** et **entropie de Shannon**.
Ce projet mesure le **temps d’exécution**, le **nombre de comparaisons** et les **accès mémoire**, tout en offrant des visualisations claires des résultats.

---

##  Objectifs
- Étudier l’impact de la taille des données, du désordre et de l’entropie sur les performances des algorithmes de tri.  
- Comparer des algorithmes classiques sur des jeux de données variés et contrôlés.  
- Visualiser les performances à l’aide de graphiques et d’animations.

---

##  Fonctionnalités
- **Génération de données** : création de jeux de données selon différentes distributions (uniforme, normale, gaussienne, exponentielle).
- **Application de désordre** : introduction d’un niveau de désorganisation (taux, blocs, ordre inverse, entropie de Shannon).  
- **Algorithmes de tri implémentés** :
  - Tri à bulles (**Bubble Sort**)
  - Tri par sélection (**Selection Sort**)
  - Tri fusion (**Merge Sort**)
  - Tri par tas (**Heap Sort**)
  - Tri par seaux (**Bucket Sort**)
- **Analyse des performances** :
  - Mesure du temps d’exécution, du nombre de comparaisons et des accès mémoire.
  - Résultats exportés en fichiers CSV.
- **Visualisation** :
  - Graphiques de comparaison (taille, taux de désordre, entropie de Shannon).
  - Figures et animations en temps réel.

---

##  Points techniques
- **Algorithmes optimisés** : Merge Sort et Heap Sort assurent une complexité stable.  
- **Structures de données** : utilisation intensive de **NumPy** pour des accès rapides et une manipulation efficace.  
- **Librairies utilisées** :  
  - **NumPy** pour la génération et la manipulation des données.  
  - **Matplotlib** pour l’affichage des graphiques comparatifs.  
  - **Pandas** pour l’analyse et le stockage des résultats.  
- **Expérimentations automatisées** : script unique pour lancer l’ensemble des tests et générer les graphiques.

---

##  Structure du projet

#### .
#### ├── data/                       # Jeux de données et résultats exportés
#### │   ├── data.csv
#### │   ├── dis_data.csv
#### │   ├── histo.csv
#### │   └── resultatAlgo.csv
#### ├── log/
#### │   └── log.csv                  # Journal des expérimentations
#### ├── script.sh                    # Script d'exécution 
#### └── src/                         
####    ├── experimentation.py       # Lancement des tests principaux
####    ├── figureShannon.py         # Graphiques en fonction de l’entropie de Shannon
####    ├── figureTaille.py          # Graphiques en fonction de la taille des données
####    ├── figureTaux.py            # Graphiques en fonction du taux de désordre
####    ├── generer.py               # Génération centralisée des données
####    ├── algotri/                 # Implémentation des algorithmes de tri
####    │   └── algorithms.py
####    ├── chart/                   # Affichage et visualisation des résultats
####    │   └── displayData.py
####    ├── disorder/                # Fonctions de désordre et entropie
####    │   └── disorder.py
####    ├── entropie/                # Calculs d’entropie de Shannon
####    │   ├── OrdreCalcul.py
####    │   └── ShannonCalcul.py
####    └── generator/               # Générateurs de données selon (distributions)
####        ├── exponentialGenerator.py
####        ├── gaussianGenerator.py
####        ├── normalGenerator.py
####        └── uniformGenerator.py


---

## ▶ Exécution

### Prérequis
- **Python 3.8+**
- Installer les dépendances nécessaires :  
```bash
pip install numpy matplotlib pandas
```

### Script automatisé pour execution 
./script.sh


---

##  Résultats
- **Bubble Sort** et **Selection Sort** deviennent rapidement inefficaces avec de grandes tailles ou un fort désordre.  
- **Heap Sort** et **Merge Sort** offrent des performances stables et prévisibles.  
- **Bucket Sort** est le plus rapide dans la plupart des scénarios, particulièrement efficace pour des données bien distribuées.

---

##  Améliorations possibles
- Intégration d’algorithmes supplémentaires (Quick Sort, Radix Sort…).  
- Interface graphique interactive pour configurer et visualiser les expérimentations.  
- Export automatique des rapports au format PDF.  

---


