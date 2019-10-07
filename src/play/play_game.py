def game(board):
    game_over = False
    turn = 0

    while not game_over:
        if turn == 0:
            selection = int(input("Enter the input of player 1 : "))
            selection -= 1
            for i in range(6, 0, -1):
                if board[i][selection] == 0:
                    board[i][selection] = 1
                    turn = 1
                    break
        else:
            selection = int(input("Enter the input of player 2 : "))
            selection -= 1
            for i in range(6, 0, -1):
                if board[i][selection] == 0:
                    board[i][selection] = 2
                    turn = 0
                    break
        print(board)
