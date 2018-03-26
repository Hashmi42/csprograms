#  File: ISBN.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:

def partial_sum(lyst):
    sum_one = []
    first_condition = True
    temp = 0
    for i in lyst:
        if first_condition:
            temp = int(i)
            first_condition = False
            sum_one.append(temp)
        else:
            if i == "X" or i == "x":
                x = 10
                temp += x
                sum_one.append(temp)
            else:
                temp += int(i)
                sum_one.append(temp)
    second_con = True
    second_sum = []
    temp2 = 0
    for j in sum_one:
        if second_con:
            temp2 = j
            second_sum.append(temp2)
            second_con = False
        else:
            temp2 += j
            second_sum.append(temp2)

    if second_sum[-1] % 11 == 0:
        return "Valid"
    elif second_sum[-1] % 11 != 0:
        return "Invalid"


def main():
    bookfile = open("isbn.txt", "r")
    out_file = open("isbnOut.txt", "w")
    list_isbn = []
    isbn_holder = []

    for lines in bookfile.readlines():
        lines = lines.strip()
        isbn_holder.append(lines)
        lines = lines.replace("-", "")
        list_isbn.append(lines)

    for i, j in zip(list_isbn, isbn_holder):
        out = out_file.write(str(j) + str(" ") + str(partial_sum(i)) + "\n")

    bookfile.close()
    out_file.close()


main()
