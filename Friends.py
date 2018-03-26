#  File: Friends.py
#  Description: check for tags
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created:
#  Date Last Modified: 11/10/17

# node class code given in class
class Node(object):
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext

    # returns a string representation of the nodes
    def __str__(self):
        return self.data

# create a user where a linked list initiated upon being called
class User():
    def __init__(self, name):
        self.name = Node(name)

    # checks to see if the user has any friends
    def noFriends(self):
        return self.name.getNext() == None

    # adds friends to the linked list of the user
    def addFriends(self, friend):
        current = self.name
        notFriends = True
        # loops through the linked list to see if the person already exists
        while current != None and notFriends:
            if current.getData() == friend:
                return False
            else:
                current = current.getNext()

        # they are not friends already then the friend is added to the linked list
        if notFriends:
            temp = Node(friend)
            temp.setNext(self.name)
            self.name = temp

        return True

    # checks to see if the user and other user are friends or not
    def areFriends(self, friend):
        current = self.name
        found = False
         # loops through the linked list and it breaks it if friend is found
        while current != None and not found:
            if current.getData() == friend:
                found = True
            else:
                current = current.getNext()

        # returns if they are friends or not
        return found

    # removes users from each others linked lists
    def removeFriend(self, friend):
        current = self.name
        previous = None
        found = False
        # loops through the linked list and searches for the friend
        while current != None and not found:
            if current.getData() == friend:
                found = True
            else:
                previous = current
                current = current.getNext()

        # if not found then it returns false
        if not found:
            return False
        # if found then it removes the friend from the linked list
        else:
            if previous == None:
                self.name = current.getNext()
                return True
            else:
                previous.setNext(current.getNext())
                return True

    # loops through the linked list and lists out all the nodes in it
    def listFriends(self):
        # if the list is empty then it returns an empty python list
        if self.name.getNext() is None:
            return []
        else:
            friends = []
            current = self.name

            # loops through the list adds all the friends in a python list and returns it to the main
            # function
            while current != None:
                name = current.getData()

                friends.append(name)

                current = current.getNext()

            return friends

    # string representation of the linked list
    def __str__(self):
        return self.name


def main():
    # reads the file
    inFile = open("FriendData.txt", "r")

    # splits the file in lines
    inFile = inFile.readlines()

    # dictionary keeps track of how many players are being created
    allUsers = {}

    # loops through the lines from the file
    for lines in inFile:
        # splits the lines into words
        lines = lines.split()
        # checks to see if the commend is "Person"
        if "Person" in lines:
            user = lines[1]
            print(lines[0], lines[1])
            # if user exists then it prints this statement and doesn't do anything
            if user in allUsers:
                print("A person with name {} already exists.".format(user), "\n")
            else:
                # adds the user in the dictionary and creates a linked list
                allUsers[user] = User(user)
                print("{} now has an account.".format(user), "\n")

        # looks for the "friend" commend to see if it should add the user
        elif "Friend" in lines:
            print(lines[0],lines[1],lines[2])
            user = lines[1]
            friend = lines[2]

            # checks to see if the user is created
            if user not in allUsers:
                print("A person with name {} does not currently exist.".format(user), "\n")
            # prevents users from adding themselves
            elif user == friend:
                print("A person cannot friend him/herself.", "\n")
            # checks to see if both of the users are created
            elif user in allUsers and friend not in allUsers:
                print("A person with name", friend, "does not currently exist.", "\n")

            elif user in allUsers and friend in allUsers:
                user = allUsers[user]
                friend = allUsers[friend]
                # checks to see if they are friends before adding the user to the linked list
                areFriends1 = allUsers[lines[1]].areFriends(lines[2])

                if areFriends1:
                    print(lines[1],"and",lines[2],"are already friends.","\n")
                # if they are not friends then the user is added to the linked list
                elif user.addFriends(lines[2]):
                    s = str(lines[1]) + " and " + str(lines[2]) + " are now friends."
                    print(s, "\n")
                    friend.addFriends(lines[1])
        # looks for the "list" commend
        elif "List" in lines:
            print(lines[0], lines[1])
            user = lines[1]

            # calls the listFriends method in the User class
            friends = allUsers[user].listFriends()

            numOfFriends = len(friends)

            # prints out if there are not friends
            if numOfFriends == 0:
                print("{} has no friends.".format(user), "\n")
            else:
                # loops through the python list and prints them out
                x = ""
                for i in range(numOfFriends):
                    if friends[i] == user:
                        pass
                    else:
                        x += " " + (friends[i])

                print(str("[") + x, "]","\n")

        # looks for the commend to "unfriend" a user
        elif "Unfriend" in lines:
            print(lines[0], lines[1], lines[2])
            user = lines[1]
            friend = lines[2]
            # checks to see if the users have accounts
            if user not in allUsers:
                print("A person with name {} does not currently exist.".format(user), "\n")
            elif friend not in allUsers:
                print("A person with name {} does not currently exist.".format(friend), "\n")
            # prevents user from unfriending themselves
            elif user == friend:
                print("A person cannot unfriend him/herself.","\n")
            # checks to see if both users are created
            elif friend in allUsers and user in allUsers:
                user1 = allUsers[user]
                user2 = allUsers[friend]

                # if they are not friends then an error is printed out
                areFriends3 = allUsers[lines[2]].areFriends(lines[1])

                if areFriends3 is False:
                    print(user, "and", friend, "aren't friends, so you can't unfriend them.", "\n")
                else:
                    # the user is unfriended the linked lists are updated
                    unfriend = user1.removeFriend(friend)
                    if unfriend:
                        s = user + " and " + friend + " are no longer friends."
                        user2.removeFriend(user)
                        print(s,"\n")

        # checks to see if it is a "query" commend
        elif "Query" in lines:
            print(lines[0], lines[1], lines[2])
            user = lines[1]
            friend = lines[2]
            # prevents player from calling itself
            if user == friend:
                print("A person cannot query him/herself.","\n")
            # makes sure that both players have accounts
            elif user not in allUsers:
                print("A person with name {} does not currently exist.".format(user), "\n")
            elif friend not in allUsers:
                print("A person with name {} does not currently exist.".format(friend), "\n")
            elif user in allUsers and friend not in allUsers:
                print("A person with name {} does not currently exist.".format(friend), "\n")
            elif user not in allUsers and friend in allUsers:
                print("A person with name {} does not currently exist.".format(user), "\n")
            # if they both then they are checked to see if they are friends
            elif user in allUsers and friend in allUsers:
                isFriends = allUsers[user].areFriends(friend)
                # prints out messages if they are friends or not
                if isFriends:
                    print(user,"and",friend,"are friends.","\n")
                else:
                    print(user, "and", friend,"are not friends.", "\n")
        # if the commend is "exit" then it breaks the loop and ends the program
        elif lines[0] == "Exit":
            print(lines[0])
            print("Exiting...")
            break



main()
