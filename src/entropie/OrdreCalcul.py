import math

def order_entropy(numbers):
    if len(numbers) < 2:
        return 0  
    transitions = []  
    
    # On parcourt la liste pour déterminer les transitions entre les éléments consécutifs
    for i in range(len(numbers) - 1):
        if numbers[i] < numbers[i+1]:
            transitions.append("↑")  
        elif numbers[i] > numbers[i+1]:
            transitions.append("↓")  
        else:
            transitions.append("=") 
    
    freq_dict = {}
    total = len(transitions)  
    for motif in transitions:
        if motif in freq_dict:
            freq_dict[motif] += 1
        else:
            freq_dict[motif] = 1
    
    entropy = 0
    for count in freq_dict.values():
        p = count / total
        entropy -= p * math.log2(p) 
    return entropy  

    
    


