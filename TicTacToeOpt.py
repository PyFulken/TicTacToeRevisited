from Sanitize import *


def TicTacToe():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    def print_board():
        print("", board[0], "|", board[1], "|", board[2])
        print("---+---+---")
        print("", board[3], "|", board[4], "|", board[5])
        print("---+---+---")
        print("", board[6], "|", board[7], "|", board[8])

    def victory_check(piece, player):
        if board[0] == board[1] == board[2] == piece or \
                board[3] == board[4] == board[5] == piece or \
                board[6] == board[7] == board[8] == piece or \
                board[0] == board[3] == board[6] == piece or \
                board[1] == board[4] == board[7] == piece or \
                board[2] == board[5] == board[8] == piece or \
                board[0] == board[4] == board[8] == piece or \
                board[2] == board[4] == board[6] == piece:
            print_board()
            print(f"Player {player} Wins!")
            return True

    def piece_placement(piece):
        while True:
            piece_target = validator("+")
            print_board()
            if piece_target > 9 or piece_target < 1:
                print("There's no such position!")
                pass
            elif board[piece_target - 1] != " ":
                print("That space is already filled! Please choose another position")
                pass
            else:
                break
        board[piece_target - 1] = piece

    for turn in range(1, 11):
        if " " not in board:
            print("You're all out of positions to place more pieces."
                  "It's a draw!")
            break
        player_list = [2, 1]
        piece_list = ["O", "X"]
        print_board()
        print(f"where will you be placing your piece, player {player_list[turn % 2]}?")
        piece_placement(piece_list[turn % 2 != 0])
        if victory_check(piece_list[turn % 2 != 0], player_list[turn % 2]):
            break


def restart_check():
    print("Would you like to play another game? (Y,N)")
    restart = input().lower()
    while restart != "y" and restart != "n":
        print("The valid inputs are either Y or N.")
        restart = input()
    while restart == "y":
        TicTacToe()
        print("Would you like to play another game? (Y,N)")
        restart = input()
    if restart == "n":
        print("\n\n\nGame Over!")


TicTacToe()
restart_check()
