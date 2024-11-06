N = int(input("Enter number of queens: "))
Board = [['_' for _ in range(N)] for _ in range(N)]

def printBoard(Board):
    for row in Board:
        for cell in row:
            print(cell, end=" ")
        print()

def isSafe(Board, row, col):
    for i in range(col):
        if Board[row][i] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if Board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if Board[i][j] == 'Q':
            return False
    return True

def SolveQueen(Board, col):
    if col >= N:
        return True
    for row in range(N):
        if isSafe(Board, row, col):
            Board[row][col] = 'Q'
            printBoard(Board)
            print(' ')
            if SolveQueen(Board, col + 1):
                return True
            Board[row][col] = '_'
            print("\n....Backtracking here...")
    return False

if SolveQueen(Board, 0) == False:
    print("\nSolution not exist")
else:
    print("\nFinal Solution:")
    printBoard(Board)
