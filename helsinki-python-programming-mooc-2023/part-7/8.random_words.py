# Write your solution here 

from random import sample

def words(n:int, beginning: str):

    matching_words = []

    returned_words = []

    with open(r"C:\Users\alexa\AppData\Local\tmc\vscode\mooc-programming-23\part07-08_random_words\src\words.txt", "r") as file:

        

        for line in file:
            line = line.strip()
            
            if line.startswith(beginning):
                if line not in matching_words:
                    matching_words.append(line)

    
    if len(matching_words) < n:
        raise ValueError("Not enough words")

    return sample(matching_words, n)





        
        

            


