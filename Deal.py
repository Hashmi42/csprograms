# File: Deal.py

# Description:

# Student Name: Logan Hashmi

# Student UT EID:Sah4334

# Course Name: CS 303E

# Unique Number: 51850

# Date Created:2-24-17

# Date Last Modified: 2-24-27

def deal():
    import random
    round = int(input("Enter the number of rounds you want to play: "))
    switch= 0
    print()
    print("     Prize       Guess       View    New Guess")
    for i in range(1,round+1):
        prize_door= random.randint(1,3)
        guess= random.randint(1,3)
        view=0

        if (prize_door==1 and guess==2) or (prize_door==2 and guess==1):
            view=3
        elif (prize_door==3 and guess==1) or (prize_door==1 and guess==3):
            view=2
        elif (prize_door==2 and guess==3) or (prize_door==3 and guess==2):
            view=1
        elif (prize_door==1 and guess==1):
            view=3
        elif (prize_door==2 and guess==2):
            view=1
        elif (prize_door==3 and guess==3):
            view=2

        newGuess=0

        for i in range(1,4):
            if i!=guess and i!=view:
                newGuess=i

        if newGuess==prize_door:
            switch+=1

        print("      ",prize_door,"         ",guess,"        ",view,"        ", newGuess)

    print()
    probability_of_switch = switch / round
    probability_of_not_switch = 1 - probability_of_switch

    print("Probability of winning if you switch = ","%.2f"%probability_of_switch)
    print("Probability of winning if you do not switch = ","%.2f"%probability_of_not_switch)

deal()
