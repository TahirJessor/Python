# create a 2 player tic tac toe
print('Tahir Muzaffar')
print('1962105')

board = [" " for col in range(10)]


def display_board(d_board):
    print(d_board[7], '|', d_board[8], '|', d_board[9])
    print("--|---|--")
    print(d_board[4], '|', d_board[5], '|', d_board[6])
    print("--|---|--")
    print(d_board[1], '|', d_board[2], '|', d_board[3])


tie = 0
win = False
while True:
    p1 = input("Player1, choose your marker(X or O): ").upper()
    if p1 == 'X':
        p2 = 'O'
        break
    elif p1 == 'O':
        p2 = 'X'
        break
    else:
        print("Invalid marker!")
print("Player 1: " + p1)
print("Player 2: " + p2)
turn = p1
display_board(board)
while not win:
    if turn == p1:
        choice = int(input("Enter your position(1-9): "))
        if choice in (1, 2, 3, 4, 5, 6, 7, 8, 9) and board[choice] == " ":
            board[choice] = turn
        else:
            print("Invalid choice!")
        turn = p2
    else:
        choice = int(input("Enter your position(1-9): "))
        if choice in (1, 2, 3, 4, 5, 6, 7, 8, 9) and board[choice] == " ":
            board[choice] = turn
        else:
            print("Invalid choice!")
        turn = p1
    display_board(board)
    if (board[7] == board[8] == board[9] == p1 or
            board[4] == board[5] == board[6] == p1 or
            board[1] == board[2] == board[3] == p1 or
            board[7] == board[4] == board[1] == p1 or
            board[8] == board[5] == board[2] == p1 or
            board[9] == board[6] == board[3] == p1 or
            board[7] == board[5] == board[3] == p1 or
            board[9] == board[5] == board[1] == p1):
        print("Player 1 wins!")
        tie += 1
        win = True
    elif (board[7] == board[8] == board[9] == p2 or
          board[4] == board[5] == board[6] == p2 or
          board[1] == board[2] == board[3] == p2 or
          board[7] == board[4] == board[1] == p2 or
          board[8] == board[5] == board[2] == p2 or
          board[9] == board[6] == board[3] == p2 or
          board[7] == board[5] == board[3] == p2 or
          board[9] == board[5] == board[1] == p2):
        print("Player 2 wins!")
        tie += 1
        win = True
    if tie == 9:
        print("It is a tie!")
        win = True
