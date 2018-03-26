#  File: sorting.py
#  Description: traverse through the trees and see if they are isomorphic
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#  Date Created: 12/3/17
#  Date Last Modified: 12/4/18



# create  a tree class
class MultiwayTree():
    # initiate a tree as soon as it is called
    def __init__(self, pyTree):
        self.data = pyTree[0]
        self.children = []
        # loops through the tree's branches and add them into sub trees
        for child in pyTree[1]:
            self.children.append(MultiwayTree(child))

    # sets the root of the node
    def setRootVal(self, root):
        self.data = root

    # this method starts out the root of the tree and then goes to the left and then right side of the tree
    def preOrder(self):
        # prints out the root
        print(str(self.getRootval()), end=" ")
        # recurse through the children nodes
        for i in range(len(self.children)):
            self.children[i].preOrder()

    # checks to see if to trees are isomporphic
    def isIsomorphicTo(self, other):
        # checks the number children in the tree and sends false if they are not the same
        if len(self.children) != len(other.children):
            return False
        # loops through both of the trees and checks to see if they have the same number of children
        for c, oc in zip(self.children, other.children):
            # if they are not then the same then it returns false
            if not c.isIsomorphicTo(oc):
                return False
        return True

    # this method returns the data of the root
    def getRootval(self):
        return self.data


def main():
    # import a package to translate a string list into an actual list
    import ast
    # opens the file
    inFile = open("MultiwayTreeInput.txt", "r")
    # reads the lines of the file
    data = inFile.readlines()
    # Tree variables to compare them
    firstTree = None
    secondTree = None
    firstCondition = True

    # counts the number of trees in the file
    counter = 1
    # loops through the lines of the file
    for tree in range(len(data)):
        # if its the very last line
        if counter == len(data):
            # prints out the number of the tree and what the line of the tree is
            print("Tree", counter, ": ", data[tree])
            # coverts string list into an actual tree
            tree = ast.literal_eval(data[tree])
            # a tree instance is created
            secondTree = MultiwayTree(tree)
            # prints out the tree number and output format
            print("Tree", counter, "preorder:   ", end=" ")
            # checks calls the preorder method
            secondTree.preOrder()
            print()
            # checks to see if the two trees are isomorphic
            if (secondTree.isIsomorphicTo(firstTree)):
                print()
                # output format
                print("Tree", counter - 1, "is isomorphic to Tree", counter)
            # if returned False then print this output
            if not (secondTree.isIsomorphicTo(firstTree)):
                print()
                print("Tree", counter - 1, "is not isomorphic to Tree", counter)
        else:
            # if it is the first tree
            if firstCondition:
                # prints out the tree number and output format
                print("Tree", counter, ": ", data[tree], end="")
                # coverts string list into an actual tree
                tree = ast.literal_eval(data[tree])
                # a tree instance is created
                firstTree = MultiwayTree(tree)
                # prints out the tree number and output format
                print("Tree", counter, "preorder:   ", end=" ")
                # checks calls the preorder method
                firstTree.preOrder()
                print()
                # Makes sure a new instance is created for the second tree
                firstCondition = False
            else:
                # prints out the tree number and output format
                print("Tree", counter, ": ", data[tree], end="")
                # coverts string list into an actual tree
                tree = ast.literal_eval(data[tree])
                # a tree instance is created
                secondTree = MultiwayTree(tree)
                # prints out the tree number and output format
                print("Tree", counter, "preorder:   ", end=" ")
                # checks calls the preorder method
                secondTree.preOrder()
                print()
                # restarts the loop to compare the two trees
                firstCondition = True

                # checks to see if the two trees are isomorphic
                if (secondTree.isIsomorphicTo(firstTree)):
                    print()
                    print("Tree", counter - 1, "is isomorphic to Tree", counter)
                # if returned False then print this output
                if not (secondTree.isIsomorphicTo(firstTree)):
                    print()
                    print("Tree", counter - 1, "is not isomorphic to Tree", counter)
        # keeps track of the number trees
        counter += 1
        print()


main()
