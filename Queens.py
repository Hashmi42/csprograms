
# solve the 8 Queens problem using back tracking
class Queens(object):
    # initialize the board
    def __init__(self, n=8):
        self.board = []
        self.n = n
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append("*")
            self.board.append(row)

    # check if no queen captures another
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=' ')
            print()

    # do a recursive solution to the problem
    def recursive_solve(self, col):
        if (col == self.n):
            return True
        else:
            for i in range(self.n):
                if (self.is_valid(i, col)):
                    self.board[i][col] = 'Q'
                    if (self.recursive_solve(col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False

    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            if (self.recursive_solve(i)):
                self.print_board()


def main():
    # create an object
    game = Queens(5)
    game.solve()


main()