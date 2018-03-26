#  File: CreditCard.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 4-4-17

#  Date Last Modified: 4-4-17

# This function checks if a credit card number is valid

def is_valid(cc_num):
    sum_double = 0
    for i in range(1, len(cc_num)):
        if i % 2 != 0:
            temp = cc_num[i] * 2
            if temp < 10:
                sum_double += temp
            else:
                temp1 = temp - 9
                sum_double += temp1
    sum_single = cc_num[0]

    for i in range(1, len(cc_num)):
        if i % 2 == 0:
            temp2 = cc_num[i]
            sum_single += temp2

    sum_all = sum_double + sum_single

    if sum_all % 10 == 0:
        return 1
    else:
        return -1


# # This function returns the type of credit card
def cc_type(d15, d14, d13, d12):
    if d15 == 6 and d14 == 0 and d13 == 1 and d12 == 1 or d15 == 6 and d14 == 4 and d13 == 4 or d15 == 6 and d14 == 5:
        return "Discover"
    elif d15 == 5 and d14 == 0 or d15 == 5 and d14 == 1 or d15 == 5 and d14 == 2 or d15 == 5 and d14 == 3 or d15 == 5 \
            and d14 == 4 or d15 == 5 and d14 == 5:
        return "MasterCard"
    elif d15 == 4:
        return "Visa"
    elif d15==0:
        if d14 == 3 and d13 == 7 or d14 == 3 and d13 == 4:
            return "American Express"
    elif d15 == 3 and d14 == 7 or d15 == 3 and d14 == 4:
        return "American Express"


def main():
    creditCard = eval(input("Enter a 15 or 16-digit credit card number: "))
    creditCards = str(creditCard)

    while (len(creditCards)) > 16 or (len(creditCards)) < 15:
        print("Not a 15 or 16-digit number")
        return -1

    cc_num = [int(i) for i in creditCards]
    cc_num.reverse()

    x = is_valid((cc_num))

    d0 = creditCard % 10
    creditCard = creditCard // 10
    d1 = creditCard % 10
    creditCard = creditCard // 10
    d2 = creditCard % 10
    creditCard = creditCard // 10
    d3 = creditCard % 10
    creditCard = creditCard // 10
    d4 = creditCard % 10
    creditCard = creditCard // 10
    d5 = creditCard % 10
    creditCard = creditCard // 10
    d6 = creditCard % 10
    creditCard = creditCard // 10
    d7 = creditCard % 10
    creditCard = creditCard // 10
    d8 = creditCard % 10
    creditCard = creditCard // 10
    d9 = creditCard % 10
    creditCard = creditCard // 10
    d10 = creditCard % 10
    creditCard = creditCard // 10
    d11 = creditCard % 10
    creditCard = creditCard // 10
    d12 = creditCard % 10
    creditCard = creditCard // 10
    d13 = creditCard % 10
    creditCard = creditCard // 10
    d14 = creditCard % 10
    creditCard = creditCard // 10
    d15 = creditCard

    if x == -1:
        print()
        print("Invalid credit card number")
        return -1
    elif x == 1:
        print()
        y = cc_type(d15, d14, d13, d12)
        print("Valid " + str(y) + " credit card number")


main()
