#  File: Craps.py

#  Description: game

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number:

#  Date Created:

#  Date Last Modified:


import random

# simulate a single round of craps and
# return 1 if player wins and 0 if he loses
def craps (rounds):
    # write the body of the code
    wins=0
    for i in range(1,rounds+1,1):
        player_roll1 = random.randint(1, 6)
        player_roll2 = random.randint(1, 6)

        if (player_roll1 + player_roll2) == 7 or (player_roll1+player_roll2) == 11:
            wins+=1

        elif (player_roll2 + player_roll1) == 2 or (player_roll2 + player_roll1) == 3 or (player_roll2 + player_roll1) == 12:
            pass

        elif (player_roll2 + player_roll1) == 4 or (player_roll2 + player_roll1) == 5 or (player_roll2 + player_roll1) == 6 \
            or (player_roll2 + player_roll1)==8 or (player_roll2 + player_roll1)==9 or (player_roll2 + player_roll1)==10:
            pointphase1 = random.randint(1, 6)
            pointphase2 = random.randint(1, 6)
            if (pointphase1 +pointphase2) == 7:
                pass

            elif (pointphase2 + pointphase1) == (player_roll1+player_roll2):
                wins+=1


    return wins

def main():
  # prompt the user to enter the number of rounds
  num_rounds = int (input ("Enter number of rounds: "))

  # compute the number of times he wins

  wins= craps(num_rounds)


  # print the result
  print ("Player wins", wins, "out of", (num_rounds), "rounds.")

main()