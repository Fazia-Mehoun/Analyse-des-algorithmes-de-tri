import matplotlib.pyplot as plt
import time
import random
import math


class algorithms:
    def __init__(self):
        pass

    def visualize_sort(self, arr, algo_name):
        """
        Visualise l'exécution d'un algorithme de tri en temps réel.
        Cette fonction permet d'afficher une visualisation interactive du tableau
        lors de l'exécution de l'algorithme de tri spécifié.
        """
        comparaisons = 0
        acces_donnees = 0
        
        # Initialisation de la figure pour afficher le graphique
        plt.ion()  # Active le mode interactif pour l'animation
        fig, ax = plt.subplots()
        ax.set_title(f"{algo_name} - Visualisation en temps réel")
        ax.set_xlabel("Index")
        ax.set_ylabel("Valeur")
        bar = ax.bar(range(len(arr)), arr, align="edge", color="skyblue")
        plt.pause(0.1)
        
        def update_display():
            """
            Met à jour le graphique pour afficher l'état actuel du tableau.
            """
            for rect, val in zip(bar, arr):
                rect.set_height(val)
            plt.draw()
            plt.pause(0.1)

        if algo_name == "Bubble Sort":
            self.bubble_sort(arr)
        elif algo_name == "Insertion Sort":
            self.insertion_sort(arr)
        elif algo_name == "Quick Sort":
            self.quick_sort(arr)
        elif algo_name == "Heap Sort":
            self.heap_sort(arr)
        elif algo_name == "Bucket Sort":
            self.bucket_sort(arr)

        plt.ioff()  
        plt.show()  

    """
    Implémente l'algorithme de tri à bulles (Bubble Sort).
    Cette méthode trie le tableau en comparant chaque élément avec son voisin.
    """
    def bubble_sort(self, arr):
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                comparaisons += 1
                acces_donnees += 2 
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    acces_donnees += 2  
        end_time = time.time()
        return arr, comparaisons, acces_donnees, end_time - start_time

    """
    Implémente l'algorithme de tri par insertion (Insertion Sort).
    Cette méthode insère chaque élément dans la sous-liste triée à gauche du tableau.
    """
    def insertion_sort(self, arr):
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            comparaisons += 1
            acces_donnees += 1  
            while j >= 0 and arr[j] > key:
                comparaisons += 1
                acces_donnees += 2  
                arr[j + 1] = arr[j]
                acces_donnees += 1  
                j -= 1
            arr[j + 1] = key
            acces_donnees += 1  
        end_time = time.time()
        return arr, comparaisons, acces_donnees, end_time - start_time

    """
    Implémente l'algorithme de tri rapide (Quick Sort).
    Cette méthode utilise un pivot pour diviser le tableau en sous-tableaux à trier récursivement.
    """
    def quick_sort(self,arr):
        if len(arr) <= 1:
            return arr, 0, 0, 0    
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()       
        stack = [(0, len(arr) - 1)]       
        while stack:
            left, right = stack.pop()
            if left >= right:
                continue
            pivot = arr[right]
            acces_donnees += 1  
            i = left - 1
            for j in range(left, right):
                comparaisons += 1
                acces_donnees += 2 
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
                    acces_donnees += 2  
            i += 1
            arr[i], arr[right] = arr[right], arr[i]
            acces_donnees += 2  
            stack.append((left, i - 1))  
            stack.append((i + 1, right))       
        end_time = time.time()
        return arr, comparaisons, acces_donnees, end_time - start_time

    """
    Implémente l'algorithme de tri par tas (Heap Sort).
    Cette méthode organise les éléments sous forme de tas binaire pour ensuite trier.
    """
    def heap_sort(self, arr):
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()
        
        def heapify(arr, n, i):
            nonlocal comparaisons, acces_donnees
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2
            if l < n and arr[l] > arr[largest]:
                comparaisons += 1
                acces_donnees += 2 
                largest = l
            if r < n and arr[r] > arr[largest]:
                comparaisons += 1
                acces_donnees += 2  
                largest = r
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                acces_donnees += 2  
                heapify(arr, n, largest)
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            acces_donnees += 2 
            heapify(arr, i, 0)
        end_time = time.time()
        return arr, comparaisons, acces_donnees, end_time - start_time

    """
    Implémente l'algorithme de tri par seaux (Bucket Sort).
    Cette méthode répartit les éléments dans des seaux et trie chaque seau individuellement.
    """
    def bucket_sort(self, arr):
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()
        if len(arr) == 0:
            end_time = time.time()
            return arr, comparaisons, acces_donnees, end_time - start_time
        min_value, max_value = min(arr), max(arr)
        bucket_count = len(arr)
        buckets = [[] for _ in range(bucket_count)]
        for num in arr:
            index = (num - min_value) * (bucket_count - 1) // (max_value - min_value)
            buckets[index].append(num)
            acces_donnees += 1  
        for i in range(bucket_count):
            buckets[i].sort()
            comparaisons += len(buckets[i]) * (len(buckets[i]) - 1) // 2  
            acces_donnees += len(buckets[i]) * 2  
        result = []
        for bucket in buckets:
            result.extend(bucket)
        end_time = time.time()
        return result, comparaisons, acces_donnees, end_time - start_time

    """
    Implémente l'algorithme de tri fusion (Merge Sort).
    Cette méthode divise récursivement le tableau en sous-tableaux puis les fusionne.
    """
    def merge_sort(self ,arr):
        if len(arr) <= 1:
            return arr, 0, 0, 0  
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()

        def merge(left, right):
            nonlocal comparaisons, acces_donnees
            sorted_arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                comparaisons += 1
                acces_donnees += 2
                if left[i] <= right[j]:
                    sorted_arr.append(left[i])
                    i += 1
                else:
                    sorted_arr.append(right[j])
                    j += 1
            sorted_arr.extend(left[i:])
            sorted_arr.extend(right[j:])
            acces_donnees += len(left) - i + len(right) - j
            return sorted_arr
        
        def merge_sort_recursive(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort_recursive(arr[:mid])
            right = merge_sort_recursive(arr[mid:])
            return merge(left, right)
        sorted_arr = merge_sort_recursive(arr)
        end_time = time.time()
        return sorted_arr, comparaisons, acces_donnees, end_time - start_time


    """
    Implémente l'algorithme de tri par sélection (Selection Sort).
    Cette méthode trouve à chaque itération le plus petit élément du tableau non trié.
    """
    def selection_sort(self ,arr):
        comparaisons = 0
        acces_donnees = 0
        start_time = time.time()
        n = len(arr)
        for i in range(n):
            min_idx = i
            acces_donnees += 1  
            for j in range(i + 1, n):
                comparaisons += 1  
                acces_donnees += 1  
                if arr[j] < arr[min_idx]:
                    min_idx = j
                    acces_donnees += 1  
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            acces_donnees += 2  
        end_time = time.time()
        return arr, comparaisons, acces_donnees, end_time - start_time
    
