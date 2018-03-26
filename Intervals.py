#  File: Intervals.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:

def main():
    in_File=open("intervals.txt","r")
    intervals=[]
    for lines in in_File.readlines():
        lines= lines.strip("\n")
        lines= lines.replace(" ", ",")
        lines= lines.strip()

        intervals.append(lines)

    lst = [eval(x) for x in intervals]
    lst.sort()
    sets=[]
    cond=True
    hi=0
    lo=0
    for i in range(len(lst)):
        if cond:
            lo=lst[i][0]
            hi=lst[i][1]
            sets.append(lo)
            sets.append(hi)
            cond=False
        else:
            if lst[i][0] in range(lo,hi) and lst[i][1]<hi:
                pass
            elif lst[i][0] in range(lo,hi) and lst[i][1]>hi:
                sets.remove(hi)
                hi=lst[i][1]
                sets.append(hi)
            elif lst[i][0] not in range(lo,hi):
                lo=lst[i][0]
                hi=lst[i][1]
                sets.append(lo)
                sets.append(hi)
    print("Non-intersecting Intervals:")
    for i in range(0,len(sets),2):
        print("("+str(sets[i])+", "+str(sets[i+1])+")")


main()

