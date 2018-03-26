#  File: Benford.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:

def main():
    # create an empty dictionary
    pop_freq = {}

    # initialize the dictionary
    pop_freq['1'] = 0
    # fill the rest
    pop_freq['2'] = 0
    pop_freq['3'] = 0
    pop_freq['4'] = 0
    pop_freq['5'] = 0
    pop_freq['6'] = 0
    pop_freq['7'] = 0
    pop_freq['8'] = 0
    pop_freq['9'] = 0

    # open file for reading
    in_file = open("./Census_2009.txt", "r")

    # read the header and ignore
    header = in_file.readline()

    # read subsequent lines
    counter=0
    for line in in_file:
        counter+=1
        line = line.strip()
        pop_data = line.split()
        # get the last element that is the population number
        pop_num = pop_data[-1]

        # make entries in the dictionary
        if pop_num[0] == "1":
            pop_freq["1"] = pop_freq["1"] + 1
        if pop_num[0] == "2":
            pop_freq["2"] = pop_freq["2"] + 1
        if pop_num[0] == "3":
            pop_freq["3"] = pop_freq["3"] + 1
        if pop_num[0] == "4":
            pop_freq["4"] = pop_freq["4"] + 1
        if pop_num[0] == "5":
            pop_freq["5"] = pop_freq["5"] + 1
        if pop_num[0] == "6":
            pop_freq["6"] = pop_freq["6"] + 1
        if pop_num[0] == "7":
            pop_freq["7"] = pop_freq["7"] + 1
        if pop_num[0] == "8":
            pop_freq["8"] = pop_freq["8"] + 1
        if pop_num[0] == "9":
            pop_freq["9"] = pop_freq["9"] + 1

    # close the file
    in_file.close()

    # write out the result
    print("Digit    Count   %")
    divisor = (pop_freq["1"] + pop_freq["2"] + pop_freq["3"]) + pop_freq["4"] \
              + pop_freq["5"] + pop_freq["6"] + pop_freq["7"] + pop_freq["8"] + pop_freq["9"]

    print("1        {}    {:.1f}".format(pop_freq["1"], ((pop_freq["1"] / divisor) * 100)))
    print("2        {}    {:.1f}".format(pop_freq["2"], ((pop_freq["2"] / divisor) * 100)))
    print("3        {}    {:.1f}".format(pop_freq["3"], ((pop_freq["3"] / divisor) * 100)))
    print("4        {}    {:.1f}".format(pop_freq["4"], ((pop_freq["4"] / divisor) * 100)))
    print("5        {}    {:.1f}".format(pop_freq["5"], ((pop_freq["5"] / divisor) * 100)))
    print("6        {}    {:.1f}".format(pop_freq["6"], ((pop_freq["6"] / divisor) * 100)))
    print("7        {}    {:.1f}".format(pop_freq["7"], ((pop_freq["7"] / divisor) * 100)))
    print("8        {}    {:.1f}".format(pop_freq["8"], ((pop_freq["8"] / divisor) * 100)))
    print("9        {}     {:.1f}".format(pop_freq["9"], ((pop_freq["9"] / divisor) * 100)))


main()
