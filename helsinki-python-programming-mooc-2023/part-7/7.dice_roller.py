# Write your solution here

from random import randint

def roll (die:str):

    die_a = [ 3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]


    if die == "A":
        return die_a[randint(0,5)]
    
    elif die == "B":
        return die_b[randint(0,5)]
    
    elif die == "C":
        return die_c[randint(0,5)]
    

def play(die1:str, die2:str, times:int):

    die_a = [ 3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]

    die1_wins = 0
    die2_wins = 0
    ties = 0

    #Assign Die 1
    if die1 == "A":
        die1 = die_a

    elif die1 == "B":
        die1 = die_b

    elif die1 == "C":
        die1 = die_c

    #Assign Die 2
    if die2 == "A":
        die2 = die_a

    elif die2 == "B":
        die2 = die_b

    elif die2 == "C":
        die2 = die_c

    for i in range(0, times):

        die1_roll = die1[randint(0,5)]

        die2_roll = die2[randint(0,5)]

        if die1_roll > die2_roll:
            die1_wins += 1

        elif die2_roll > die1_roll:
            die2_wins += 1
        
        elif die1_roll == die2_roll:
            ties +=1 
    
    return (die1_wins, die2_wins, ties)
    





