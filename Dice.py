#  File: Dice.py
#  Description: Program imitates random rolling of 2 six-sided dice
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 9/12/17
#  Date Last Modified: 9/15/17

def main():
    import random
    random.seed(1314)

    # ask for user's input
    trials = int(input("How many times do you want to roll the dice? "))

    # create a dictionary to keep track of dice rolls
    results = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}

    # loop through the random function by the amount trials user wants and saves that sum into the dictionary
    for i in range(1, trials + 1):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        sumnum = die1 + die2
        results[sumnum]+=1

    # create a list of the values for the result print out
    resultOutput = list(results.values())

    # divide values by 10 for trials greater 100 to keep the chart symmetric
    if trials > 100:
        for j in results:
            results[j] = results[j] // 10

    # create a list from the dictionary values for the histogram
    listOfValus = list(results.values())

    # print out the results
    print("Results :",resultOutput,"\n")

    # find the greatest and lowest values of the trials
    hi = max(listOfValus)
    low = min(listOfValus)

    # loop through the values and print out the histogram
    if low>0:
        for i in range(hi,low-1,-1):
            print("|", end="")
            for j in range(len(listOfValus)):
                if listOfValus[j]>=i:
                    print("  *",end="")
                else:
                    print("  ",end =" ")
            print()
    else:
        for i in range(hi,low,-1):
            print("|", end="")
            for j in range(len(listOfValus)):
                if listOfValus[j]>=i:
                    print("  *",end="")
                else:
                    print("  ",end =" ")
            print()

    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9  10 11 12")


main()
