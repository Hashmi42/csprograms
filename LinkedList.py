#  File: LinkedList.py
#  Description: check for tags
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 10/22/17
#  Date Last Modified: 10/27/17

# Node class given in class

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None  # pointer to a node

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newData):
        self.data = newData

    def setNext(self,newNext):
        self.next = newNext


class LinkedList():
    # linked class is initiated with an empty head pointer
    def __init__(self):
        self.head = None

    # string representation of nodes 10 in each line
    def __str__(self):
        current = self.head
        emptystr = ""
        counter = 0
        while current != None: # checks when to stop the loop
            if counter == 9:
                # after the 10th item it creates a new line of nodes
                emptystr += " " + str(current.getData()) + " " +"\n"
                current = current.getNext()
                counter = 0
            else:
                # addes the node to an empty string and keeps track of the count
                counter+=1
                emptystr+=" "+str(current.getData()) + " "
                current = current.getNext()

        return emptystr

    def addFirst(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    # Add an item to the beginning of the list

    def addLast(self, item):
        # this checks to see if the node is empty
        if self.head is None:
            self.head = Node(item)
        else:
            prevNode = self.head

            # loops through the nodes to the end of the list
            while True:
                if prevNode.next is None:
                    break
                prevNode = prevNode.next

            prevNode.next = Node(item)

    # this method adds the nodes in order
    def addInOrder(self, item):
        current = self.head
        previous = None
        stop = False

        while not stop:
            # checks the nodes to see when to break it
            if current is None:
                break
            # check to see if the data is greater the item
            # if it's true then it changes the variable and stops the loop
            elif current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        # assignment of the nodes
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


    # Returns the number of items in the list
    def getLength(self):
        current = self.head
        counter = 0 #keeps track of the items in the node list

        # loops through the list and keeps count
        while current != None:
            counter+=1
            current = current.getNext()

        return counter


    # finds items in a unordered list
    def findUnordered(self, item):
        current = self.head
        found = False
         # loops through the list to see if data is inside the list
        while current!= None and not found:
            # if the node is equal to the item then it changes the variable to true
            if current.getData() == item:
                found = True
            else:
                # reassigns to the next node
                current = current.getNext()
        # returns true or false
        return found

    # looks for an item in a ordered list
    def findOrdered(self, item):
        current = self.head
        found = False
        stop = False
        # loops through the node
        while current != None and not stop and not found:
            # if the data is equal to the item then it changes found to True
            if current.getData() == item:
                found = True
            else:
                # at any point if the data is greater than the item and not found it stops it stops loop
                if current.getData() > item:
                    stop = True
                current = current.getNext()

        return found

    # deletes an item from a list
    def delete(self, item):
        current = self.head
        found = False
        previous = None

        while current.next != None and not found:
            # if the data is equal to item then it ends the loop
            if current.getData() == item:
                found = True
            else:
                # continues the loop
                previous = current
                current = current.getNext()

        # condition one item lists
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        return found


    def copyList(self):
        newList = self


        return newList

    #
    # # Return a new linked list that's a copy of the original,
    # #    made up of copies of the original elements


    # def reverseList(self):
    #     previous = self.head
    #     current = self.head.getNext()
    #     nextnode = None
    #     while current != None:
    #         current = current.setNext(previous)
    #         previous =






    # Return a new linked list that contains the elements of the
    #    original list in the reverse order.
    #

    def orderList(self):

        # current = self.head
        #
        # nextnode = self.head.getNext()
        # stop = False
        #
        # while not stop:
        #     if current.getData() > nextnode.getData():
        #         previous = current
        #         current = nextnode
        #         current.setNext (previous)
        #     if nextnode is None:
        #         stop= True
        #     else:
        #         current = current
        #         nextnode = current.getNext()

        return self

    # Return a new linked list that contains the elements of the
    #    original list arranged in ascending (alphabetical) order.
    #    Do NOT use a sort function:  do this by iteratively
    #    traversing the first list and then inserting copies of
    #    each item into the correct place in the new list.

    # checks to see if the list is ordered or not
    def isOrdered(self):

        current = self.head
        nextnode = self.head.getNext()

        isOrd = True

        # if the second data is less than first then it it changes it to false

        if current.getData() > nextnode.getData():
            isOrd = False

        # returns true or false
        return isOrd

    # check to see if the linked list is empty
    def isEmpty(self):

        return self.head == None


    def mergeList(self, b):
        current = self.head
        new_list = current
        listb = b

        while current.getNext() != None:

            current = current.getNext()
            new_list.setNext(b)

            new_list.setData(current)



    # # Return an ordered list whose elements consist of the
    # #    elements of two ordered lists combined.
    #

    # checks to see if the two lists are equal or not
    def isEqual(self, b):

        return self == b




    # Test if two lists are equal, item by item, and return True.
    #
    def removeDuplicates(self):
        current = self.head
        second = self.head
        previous = None
        x = self.getLength()

        for i in range(x):
            for j in range(x):
                if current.getData() == second.getData():
                    next2 = second.getNext()
                    previous.setNext(next2)
                else:
                    previous = second
                    second = second.getNext()

        return current



    # Remove all duplicates from a list, returning a new list.
    #    Do not change the order of the remaining elements.




def main():
    print("\n\n***************************************************************")
    print("Test of addFirst:  should see 'node34...node0'")
    print("***************************************************************")
    myList1 = LinkedList()
    for i in range(35):
        myList1.addFirst("node" + str(i))

    print(myList1)

    print("\n\n***************************************************************")
    print("Test of addLast:  should see 'node0...node34'")
    print("***************************************************************")
    myList2 = LinkedList()

    for i in range(35):
        myList2.addLast("node" + str(i))

    print(myList2)



    print("\n\n***************************************************************")
    print("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
    print("***************************************************************")
    greekList = LinkedList()
    greekList.addInOrder("gamma")
    greekList.addInOrder("delta")
    greekList.addInOrder("alpha")
    greekList.addInOrder("epsilon")
    greekList.addInOrder("omega")
    print(greekList)

    print("\n\n***************************************************************")
    print("Test of getLength:  should see 35, 5, 0")
    print("***************************************************************")
    emptyList = LinkedList()
    print("   Length of myList1:  ", myList1.getLength())
    print("   Length of greekList:  ", greekList.getLength())
    print("   Length of emptyList:  ", emptyList.getLength())

    print("\n\n***************************************************************")
    print("Test of findUnordered:  should see True, False")
    print("***************************************************************")
    print("   Searching for 'node25' in myList2: ", myList2.findUnordered("node25"))
    print("   Searching for 'node35' in myList2: ", myList2.findUnordered("node35"))
    #
    print("\n\n***************************************************************")
    print("Test of findOrdered:  should see True, False")
    print("***************************************************************")
    print("   Searching for 'epsilon' in greekList: ", greekList.findOrdered("epsilon"))
    print("   Searching for 'omicron' in greekList: ", greekList.findOrdered("omicron"))
    #
    print("\n\n***************************************************************")
    print("Test of delete:  should see 'node25 found', 'node34 found',")
    print("   'node0 found', 'node40 not found'")
    print("***************************************************************")
    print("   Deleting 'node25' (random node) from myList1: ")
    if myList1.delete("node25"):
        print("      node25 found")
    else:
        print("      node25 not found")
    print("   myList1:  ")
    print(myList1)

    print("   Deleting 'node34' (first node) from myList1: ")
    if myList1.delete("node34"):
        print("      node34 found")
    else:
        print("      node34 not found")
    print("   myList1:  ")
    print(myList1)
    #
    print("   Deleting 'node0'  (last node) from myList1: ")
    if myList1.delete("node0"):
        print("      node0 found")
    else:
        print("      node0 not found")
    print("   myList1:  ")
    print(myList1)
    #
    print("   Deleting 'node40' (node not in list) from myList1: ")
    if myList1.delete("node40"):
        print("      node40 found")
    else:
        print("   node40 not found")
    print("   myList1:  ")
    print(myList1)
    # #
    print("\n\n***************************************************************")
    print("Test of copyList:")
    print("***************************************************************")
    greekList2 = greekList.copyList()
    print("   These should look the same:")
    print("      greekList before delete:")
    print(greekList)
    print("      greekList2 before delete:")
    print(greekList2)
    greekList2.delete("alpha")
    print("   This should only change greekList2:")
    print("      greekList after deleting 'alpha' from second list:")
    print(greekList)
    print("      greekList2 after deleting 'alpha' from second list:")
    print(greekList2)
    greekList.delete("omega")
    print("   This should only change greekList1:")
    print("      greekList after deleting 'omega' from first list:")
    print(greekList)
    print("      greekList2 after deleting 'omega' from first list:")
    print(greekList2)

    # print("\n\n***************************************************************")
    # print("Test of reverseList:  the second one should be the reverse")
    # print("***************************************************************")
    # print("   Original list:")
    # print(myList1)
    # print("   Reversed list:")
    # myList1Rev = myList1.reverseList()

    # print(myList1Rev)
    #
    print("\n\n***************************************************************")
    print("Test of orderList:  the second list should be the first one sorted")
    print("***************************************************************")
    planets = LinkedList()
    planets.addFirst("Mercury")
    planets.addFirst("Venus")
    planets.addFirst("Earth")
    planets.addFirst("Mars")
    planets.addFirst("Jupiter")
    planets.addFirst("Saturn")
    planets.addFirst("Uranus")
    planets.addFirst("Neptune")
    planets.addFirst("Pluto?")

    print("   Original list:")
    print(planets)
    print("   Ordered list:")
    orderedPlanets = planets.orderList()
    print(orderedPlanets)
    #
    print("\n\n***************************************************************")
    print("Test of isOrdered:  should see False, True")
    print("***************************************************************")
    print("   Original list:")
    print(planets)
    print("   Ordered? ", planets.isOrdered())
    orderedPlanets = planets.orderList()
    print("   After ordering:")
    print(orderedPlanets)
    print("   ordered? ", orderedPlanets.isOrdered())

    print("\n\n***************************************************************")
    print("Test of isEmpty:  should see True, False")
    print("***************************************************************")
    newList = LinkedList()
    print("New list (currently empty):", newList.isEmpty())
    newList.addFirst("hello")
    print("After adding one element:", newList.isEmpty())

    print("\n\n***************************************************************")
    print("Test of mergeList")
    print("***************************************************************")
    list1 = LinkedList()
    list1.addLast("aardvark")
    list1.addLast("cat")
    list1.addLast("elephant")
    list1.addLast("fox")
    list1.addLast("lynx")
    print("   first list:")
    print(list1)
    list2 = LinkedList()
    list2.addLast("bacon")
    list2.addLast("dog")
    list2.addLast("giraffe")
    list2.addLast("hippo")
    list2.addLast("wolf")
    print("   second list:")
    print(list2)
    print("   merged list:")
    list3 = list1.mergeList(list2)
    print(list3)
    #
    print("\n\n***************************************************************")
    print("Test of isEqual:  should see True, False, True")
    print("***************************************************************")
    print("   First list:")
    print(planets)
    planets2 = planets.copyList()
    print("   Second list:")
    print(planets2)
    print("      Equal:  ", planets.isEqual(planets2))
    print(planets)
    planets2.delete("Mercury")
    print("   Second list:")
    print(planets2)
    print("      Equal:  ", planets.isEqual(planets2))
    print("   Compare two empty lists:")
    emptyList1 = LinkedList()
    emptyList2 = LinkedList()
    print("      Equal:  ", emptyList1.isEqual(emptyList2))

    print("\n\n***************************************************************")
    print("Test of removeDuplicates:  original list has 14 elements, new list has 10")
    print("***************************************************************")
    dupList = LinkedList()
    print("   removeDuplicates from an empty list shouldn't fail")
    newList = dupList.removeDuplicates()
    print("   printing what should still be an empty list:")
    print(newList)
    dupList.addLast("giraffe")
    dupList.addLast("wolf")
    dupList.addLast("cat")
    dupList.addLast("elephant")
    dupList.addLast("bacon")
    dupList.addLast("fox")
    dupList.addLast("elephant")
    dupList.addLast("wolf")
    dupList.addLast("lynx")
    dupList.addLast("elephant")
    dupList.addLast("dog")
    dupList.addLast("hippo")
    dupList.addLast("aardvark")
    dupList.addLast("bacon")
    print("   original list:")
    print(dupList)
    print("   without duplicates:")
    newList = dupList.removeDuplicates()
    print(newList)


main()







