#  File: Grid.py

#  Description:

#  Student Name: Logan Hashmi

#  Student UT EID: Sah4334

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created:

#  Date Last Modified:

def main():
    # open the file
    in_file = open("./grid.txt", "r")

    # read the dimension of the grid
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)

    # create an empty grid
    grid = []

    # populate that grid
    for i in range(dim):
        line = in_file.readline()
        line = line.strip()
        row = line.split()
        for j in range(dim):
            row[j] = int(row[j])
        grid.append(row)

    # read each row in blocks of four
    row_prod = 1
    for row in grid:
        for i in range(dim - 3):
            prodrow=1
            for j in range(i, i + 4):
                prodrow = prodrow * row[j]
                if prodrow > row_prod:
                    row_prod = prodrow

    # read each column in blocks of four
    col_prod = 1
    for j in range(dim):
        for i in range(dim - 3):
            prodcol = 1
            for k in range(i, i + 4):
                prodcol = prodcol*(grid[k][j])
                if prodcol>col_prod:
                    col_prod=prodcol

    # go along all diagonals L to R in blocks of 4
    diag_prod = 1
    for i in range(dim - 3):
        for j in range(dim - 3):
            proddiag = 1
            for k in range(4):
                proddiag = proddiag*grid[i + k][j + k]
                if proddiag>diag_prod:
                    diag_prod=proddiag

    #go along all diagonals R to L in blocks of 4
    right_diag_prod=1
    for i in range(dim-3):
        for j in range(dim-1,3,-1):
            prod_right=1
            for k in range(4):
                prod_right=prod_right*grid[i+k][j-k]
                if prod_right>right_diag_prod:
                    right_diag_prod=prod_right

    #list of products
    lyst_prod=[]
    lyst_prod.append(row_prod)
    lyst_prod.append(col_prod)
    lyst_prod.append(diag_prod)
    lyst_prod.append(right_diag_prod)
    lyst_prod.sort()
    print("The greatest product is "+str(lyst_prod[-1])+".")

    in_file.close()

main()
