#  File: DNA.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number:51850

#  Date Created:

#  Date Last Modified: 3-25-17
def main():
    in_file = open("./" "dna.txt", "r")

    num_pairs = in_file.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

    print("Longest Common Sequences")
    print("")


    for i in range(num_pairs):

        print("Pair "+str(i+1)+" : ", end="")

        str1 = in_file.readline()
        str2 = in_file.readline()

        str1 = str1.strip()
        str2 = str2.strip()

        str1 = str1.upper()
        str2 = str2.upper()

        strand1= str1
        strand2= str2

        if (len(str2)) > (len(str1)):
            strand1,strand2=str2 , str1

        window = len(strand2)
        finished = False
        while (window > 1 and not finished):
            counter = 0
            while (counter + window) <= (len(strand2)):
                sub_strand = strand2[counter:counter + window]

                if sub_strand in strand1:
                    print(sub_strand, end=" \n\t\t ")
                    finished = True
                counter += 1
            window -= 1
        if not finished:
            print("No common Sequence Found")
        print(end="\n")

    in_file.close()

main()