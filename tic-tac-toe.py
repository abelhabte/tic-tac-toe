the_board = {"1,1": ' ', "1,2": ' ', "1,3": ' ',
             "2,1": ' ', "2,2": ' ', "2,3": ' ',
             "3,1": ' ', "3,2": ' ', "3,3": ' '}

board_keys = []

for key in the_board:
    board_keys.append(key)


def print_board(board):
    print(board["1,1"] + "|" + board["1,2"] + "|" + board["1,3"])
    print("-+-+-")
    print(board["2,1"] + "|" + board["2,2"] + "|" + board["2,3"])
    print("-+-+-")
    print(board["3,1"] + "|" + board["3,2"] + "|" + board["3,3"])


def game():
    turn = 'X'
    count = 0

    for i in range(9):
        print_board(the_board)
        print("It's your turn, " + turn + ". Move to which place?")
        move = input()

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        if count >= 5:
            if the_board["1,1"] == the_board["1,2"] == the_board["1,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["2,1"] == the_board["2,2"] == the_board["2,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["3,1"] == the_board["3,2"] == the_board["3,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["1,1"] == the_board["2,1"] == the_board["3,1"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["1,2"] == the_board["2,2"] == the_board["3,2"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["1,3"] == the_board["2,3"] == the_board["3,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["1,1"] == the_board["2,2"] == the_board["3,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return
            elif the_board["3,1"] == the_board["2,2"] == the_board["1,3"] != ' ':
                print_board(the_board)
                print("\nGame Over\n")
                print("----" + turn + " won. ----")
                return

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            return

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    restart = input("Do you want to play again? (y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            the_board[key] = ' '

        game()


if __name__ == "__main__":
    game()