#  File: Hailstone.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 2-27-17

#  Date Last Modified: 2-27-17

def hailstone(x, y):
    num_count = 0
    num = x
    x = x
    while True:
        if x == 1:
            break
        elif x % 2 != 0:
            x = (x * 3) + 1

        else:
            x -= x // 2
        num_count += 1
    return num, num_count

def main():
    x = int(input("Enter starting number of the range:  "))
    y = int(input("Enter ending number of the range: "))
    while x <= 0 or y <= 0 or x > y:
        x = int(input("Enter starting number of the range:  "))
        y = int(input("Enter ending number of the range: "))

    number = 0
    rounds = 0

    for i in range(x, y + 1):
        F, T = hailstone(i, y)

        if T >= rounds:
            rounds = T
            number = F

    print("The number ", number, "has the longest cycle length of ", rounds)

main()
