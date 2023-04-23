# Write your solution here

def factorials(n: int):

    dictionary = {}
    z = 1
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            
            k = j
            z *= k
            
            k -= 1
        
        dictionary[i] = z
        z = 1
        
    return dictionary 