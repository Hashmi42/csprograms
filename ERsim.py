#  File: htmlChecker.py
#  Description: check for tags
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 10/18/17
#  Date Last Modified: 10/19/17

# implementation of a queue
class Queue(object):
    # initiate an empty list whenever the class is called
    def __init__(self):
        self.patients = []

    # checks to see if there is anything on the list
    def isEmpty(self):
        return self.patients == []

    # adds the item to the front of the list
    def add(self, item):
        self.patients.append(item)

    # deletes the first item on the list
    def treat(self):
        return self.patients.pop(0)

    def peak(self):
        return self.patients[0]

    def __str__(self):
        temp = str(self.patients)
        return temp

def main():
    # create a queue for each line
    critical = Queue()
    serious = Queue()
    fair = Queue()

    # open the file
    file = open("ERsim.txt", "r")

    # loops the through the file until it is broken
    for lines in file.readlines():
        # splits the lines in between empty spaces
        lines = lines.split()
        # checks to see what type of commend it is
        if lines[0] == "add":
            # checks the type of line it is supposed to be added to (same process for all different lines)
            if lines[1] == "Critical":
                # updates the list
                critical.add(lines[2])
                # prints a string representation in the format requested
                print("Commend: Add patient " + str(lines[2]) + " to " + str(lines[1]) + " queue")
                print()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))
            elif lines[1] == "Serious":
                serious.add(lines[2])
                print("Commend: Add patient " + str(lines[2]) + " to " + str(lines[1]) + " queue")
                print()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))
            elif lines[1] == "Fair":
                fair.add(lines[2])
                print("Commend: Add patient " + str(lines[2]) + " to " + str(lines[1]) + " queue")
                print()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))

        # checks for treat next
        elif lines[0] == "treat" and lines[1] == "next":
            # checks to see if all lists age empty
            if critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                print("Commend: Treat next patient")
                print("   No patients in queues")

            # checks to see if the critical line is empty or not
            elif critical.isEmpty():
                # checks to see if the serious line is empty or not
                if serious.isEmpty():
                    # checks to see if the fair line is empty or not
                    if fair.isEmpty():
                        print("No patients available in that condition.")
                    else:
                        # if serious is empty, the commend goes to the fair line and prints the string format
                        print("Commend: Treat next patient")
                        print()
                        print("   Treating", fair.peak(), "Fair queue")
                        # pops out the patient on the front of the line
                        fair.treat()
                        print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                            serious) + "\n" + "   Critical: " + str(critical))
                else:
                    # does the same thing as above if the critical line is empty
                    print("Commend: Treat next patient")
                    print()
                    print("   Treating", serious.peak(), "Serious queue")
                    serious.treat()
                    print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                        serious) + "\n" + "   Critical: " + str(critical))
            # checks to see if serious is empty or not
            elif serious.isEmpty():
                if fair.isEmpty():
                    print("No patients available in that condition.")
                else:
                    # if serious is empty, the commend goes to the fair line and prints the string format
                    print("Commend: Treat next patient")
                    print()
                    print("   Treating", fair.peak(), "Fair queue")
                    fair.treat()
                    print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                        serious) + "\n" + "   Critical: " + str(critical))
            # checks to see if fair lines is empty or not
            elif fair.isEmpty():
                print("Command: Treat next patient")
                print("   No patients in queues")
            # if critical line is not empty it treats the patients in the critical line
            else:
                print("Commend: Treat next patient")
                print()
                print("   Treating", critical.peak(), "Critical queue")
                critical.treat()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))

        # checks for treat and a particular stated condition
        # same logic as the above treat cases
        elif lines[0] == "treat" and lines[1] == "Serious":
            if serious.isEmpty():
                print("Command: Treat next patient on Critical queue")
                print("No patients in queue")
            else:
                print("Command: Treat next patient on Serious queue")
                print()
                print("   Treating", serious.peak(), "Serious queue")
                serious.treat()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))

        elif lines[0] == "treat" and lines[1] == "Critical":
            if critical.isEmpty():
                print("Command: Treat next patient on Critical queue")
                print("No patients in queue")
            else:
                print("Command: Treat next patient on Critical queue")
                print()
                print("   Treating", critical.peak(), "Critical queue")
                critical.treat()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))

        elif lines[0] == "treat" and lines[1] == "Fair":
            if fair.isEmpty():
                print("Command: Treat next patient on Critical queue")
                print("No patients in queue")
            else:
                print("Command: Treat next patient on Fair queue")
                print()
                print("   Treating", fair.peak(), "Fair queue")
                fair.treat()
                print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                    serious) + "\n" + "   Critical: " + str(critical))

        # checks to see to see if the commend is "treat all"
        elif lines[0] == "treat" and lines[1] == "all":
            print("Command: Treat all patients")
            print()
            # a condition for the while loop
            notEmpty = True
            # loops through the treating all cases until all the lists are empty
            while notEmpty:
                # if the condition is met then it goes through the same logic as the previous treat cases
                if not critical.isEmpty():
                    print("   Treating", critical.peak(), "Critical queue")
                    critical.treat()
                    print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                        serious) + "\n" + "   Critical: " + str(critical))
                    print()

                # if the condition is met then it goes through the same logic as the previous treat cases
                if not serious.isEmpty():
                    print("   Treating", serious.peak(), "Serious queue")
                    serious.treat()
                    print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                        serious) + "\n" + "   Critical: " + str(critical))
                    print()

                # if the condition is met then it goes through the same logic as the previous treat cases
                elif not fair.isEmpty():
                    print("   Treating", fair.peak(), "Fair queue")
                    fair.treat()
                    print("   Queues are:" + "\n" + "   Fair: " + str(fair) + "\n" + "   Serious: " + str(
                        serious) + "\n" + "   Critical: " + str(critical))
                    print()
                # if all lines are empty then it breaks the loop
                elif critical.isEmpty() and serious.isEmpty() and fair.isEmpty():
                    print("   No patients in queues")
                    print()
                    notEmpty = False
        # looks for exit commend and then ends the program
        elif lines[0] == "exit":
            print("Commend: Exit")
            break

main()
