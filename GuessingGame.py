#  File: GuessingGame.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:


def main():
    print("Think of a number between 1 and 100 inclusive."
          " And I will guess what it is in 7 tries or less.")
    print()
    prompt = str(input("Are you ready? (y/n): "))
    condition1 = prompt != "y"
    condition2 = prompt != "n"
    while condition1 and condition2:
        prompt = str(input("Are you ready? (y/n): "))
        if prompt == "y" or prompt == "n":
            condition2 = False
            condition1 = False
    if prompt == "n":
        print()
        print("Bye")
        return -1
    counter = 1
    guess = 50
    hi = 100
    lo = 1
    print()
    while True:
        if counter == 8:
            print("Either you guessed a number out of range or you had an incorrect entry.")
            return -1
        print()
        print("Guess " + str(counter) + ": The number you thought was " + str(guess))
        prompt = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
        cond1 = prompt != "1"
        cond2 = prompt != "-1"
        cond3 = prompt != "0"
        while cond1 and cond2 and cond3:
            prompt= input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
            if prompt == "1" or prompt == "-1" or prompt== "0":
                cond1 = False
                cond2 = False
                cond3 = False
        print()
        if prompt == "1":
            hi = guess
            guess = (hi + lo) // 2
        if prompt == "-1":
            lo = guess
            guess = ((hi + lo) // 2)
        if prompt == "0":
            print("Thank you for playing the Guessing Game.")
            return -1
        counter += 1
main()
