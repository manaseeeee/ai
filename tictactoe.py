def ConstBoard(board):
    print("Current State Of Board:\n")
    for i in range(9):
        if i > 0 and i % 3 == 0:
            print("\n")
        print("- " if board[i] == 0 else "O " if board[i] == 1 else "X ", end=" ")
    print("\n")

def UserTurn(board):
    pos = int(input("Enter X's position from [1...9]: "))
    if board[pos-1] != 0:
        print("Wrong Move!")
        exit(0)
    board[pos-1] = -1

def minimax(board, player):
    x = analyzeboard(board)
    if x != 0:
        return x * player
    pos, value = -1, -2
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -minimax(board, -player)
            if score > value:
                value, pos = score, i
            board[i] = 0
    return 0 if pos == -1 else value

def CompTurn(board):
    pos, value = -1, -2
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if score > value:
                value, pos = score, i
    board[pos] = 1

def analyzeboard(board):
    for a, b, c in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if board[a] != 0 and board[a] == board[b] == board[c]:
            return board[c]
    return 0

def main():
    print("Computer : O Vs. You : X")
    player = int(input("Enter to play 1(st) or 2(nd): "))
    board = [0] * 9
    for i in range(9):
        if analyzeboard(board) != 0:
            break
        if (i + player) % 2 == 0:
            CompTurn(board)
        else:
            ConstBoard(board)
            UserTurn(board)
    x = analyzeboard(board)
    ConstBoard(board)
    print("Draw!" if x == 0 else "X Wins!" if x == -1 else "O Wins!")

main()
