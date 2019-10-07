from board.create_board import create
from play.play_game import game

if __name__=="__main__":
    board = create()
    game(board)
    print(board)
