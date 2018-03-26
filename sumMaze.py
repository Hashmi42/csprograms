#  File: sumMaze.py
#  Description: solve the maze
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#
#  Date Created: 11/14/17
#  Date Last Modified:

# Create a state class
class State():
    # these are the class variables for each puzzle
    targetValue = 0
    grid = None
    gridSizeRow = 0
    gridSizeCol = 0
    pathHistory = []
    startRow = 0
    startCol = 0
    newSum = 0
    solved = False
    firstCondition = True
    endRow = 0
    endCol = 0

    # prints out a 2D representation of the grid
    def __str__(self):
        gridstr = "Grid:"
        colCounter = -1
        rowCounter = -1
        #loops through the grid list
        for i in self.grid:
            # adds a new line after each row
            gridstr+= "\n"
            # keeps track of the columns
            colCounter+=1
            rowCounter = -1
            # loops through the inner list
            for j in i:
                # updates the rowcounter
                rowCounter+=1
                #replaces all the variables visited with X's
                if int(j) in self.pathHistory:
                    gridstr += "   " + str("X") + "  "
                # it replaces the current with a X and adds the element to the history
                elif int(self.startRow) == int(colCounter) and int(self.startCol) == int(rowCounter):
                    gridstr += "   " + str("X") + "  "
                    self.pathHistory.append(int(j))
                    # updates the total sum
                    self.newSum += int(j)

                # spacing formats
                elif int(j) > 9:
                    gridstr+= "   " + j +" "
                else:
                    gridstr += "   " + j +"  "

        #adds the history and starting point to the print statement
        gridstr+= "\n" + "history: "+ str(self.pathHistory)
        gridstr += "\n" + "starting point: " + "(" + str(self.startRow)+","+str(self.startCol)+ ")"
        gridstr += "\n" + "sum so far: "+ str(self.newSum)
        return gridstr

def solve(stateInstance):
    grid = stateInstance

    # loops through until the puzzle gets solved
    while not grid.solved:
        print(grid,"\n")
        print("Is this a goal state?")
        # checks to see if the current state is the starting point
        if int(grid.newSum) == int(grid.targetValue):
            print("Solution found!")
            print(grid.pathHistory)
        else:
            print("No. Can I move right?")

            if int(grid.newSum) > int(grid.targetValue):
                print("No. Target exceeded:  abandoning path")
                # if it goes over the target then it pops the last element added to the pathhistory
                x = grid.pathHistory[-1]
                grid.newSum-=x
                grid.pathHistory.pop(-1)
                grid.pathHistory.pop(-1)
                
            # checks to see if you can move right
            elif int(grid.startCol) < 5 and isValid(grid,grid.gridSizeRow,grid.gridSizeCol,grid.startRow,grid.startCol+1):

                print("Yes!")
                grid.startCol+=1 # updates the starting column

            # checks to see if moving up is a possible action
            elif int(grid.startRow) > -1 and isValid(grid, grid.gridSizeRow, grid.gridSizeCol, grid.startRow, grid.startCol):
                print("No. Can I move up?")
                print("Yes!")
                grid.startRow -=1 #updates the starting row


            elif int(grid.startRow) < 5 and isValid(grid, grid.gridSizeRow, grid.gridSizeCol, grid.startRow, grid.startCol):
                print("No. Can I move down?")
                grid.startRow +=1 #updates the starting row

            # check to see if you could move down
            elif int(grid.startCol) < 5 and isValid(grid, grid.gridSizeRow, grid.gridSizeCol,grid.startRow, grid.startCol+1):
                print("No. Can I move to the right?")
                grid.startCol -=1 #updates the starting column


# checks to see if the move is valid or no
def isValid(currGrid, gridRow, gridCol, startRow, startCol):
    if int(startRow) < int(gridRow) and int(startCol) < int(gridCol) and int(currGrid.newSum) < int(currGrid.targetValue):
        return True

    return False




def main():
    # opens a file and reads it
    inFile = open("mazedata.txt","r")

    inFile = inFile.readlines()

    gridList = []

    targetValue = 0
    gridrows = 0
    gridcols = 0
    startrow = 0
    startcol = 0
    endrow = 0
    endcol = 0

    first_seven = True

    # loops through the file and populates the variables and the grid
    for lines in inFile:
        lines = lines.split()
        # checks for the first line with the important info
        if first_seven:
            targetValue = lines[0]
            gridrows = lines[1]
            gridcols = lines[2]
            startrow = int(lines[3])
            startcol = int(lines[4])
            endrow = lines[5]
            endcol = lines[6]
            first_seven = False
        else:
            # then the grid is populated
            gridList.append(lines)

    # creates a state object
    thisState = State()
    # populates the class variables with the corresponding variables taken from the file
    thisState.grid = gridList
    thisState.gridSizeRow = gridrows
    thisState.gridSizeCol = gridcols
    thisState.startCol = startcol
    thisState.startRow = startrow
    thisState.targetValue = targetValue
    # calls the solve function 
    solve(thisState)


main()


