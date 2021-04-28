class NQ:
    def __init__(self, size):
        self.n = size
        self.board = self.generateBoard()

    def solve(self):
        if self.__util(0) == False:
            print("Solution does not exist")

        self.printBoard()

    def __util(self, col):
        if col >= self.n:
            return False

        for row in range(self.n):
            if self.__isSafe(row, col):
                self.board[row][col] = 1

                if self.__util(col + 1) == True:
                    return True

                self.board[row][col] = 0

    def __isSafe(self, row, col):
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        return True

    def generateBoard(self):
        temp_board = []
        for i in range(self.n):
            temp = []
            for j in range(self.n):
                temp.append(0)
            temp_board.append(temp)
        return temp_board

    def printBoard(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j], end=" ")
            print()


def main():
    Nqueen = NQ(4)
    Nqueen.solve()
    Nqueen.printBoard()


if __name__ == "__main__":
    main()
