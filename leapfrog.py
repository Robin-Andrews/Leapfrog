"""
Leapfrog Game
Robin Andrews - https://compucademy.net
"""

GAP = "_"
A = "A"
B = "B"
NUM_LILLYPADS = 5
if NUM_LILLYPADS % 2 != 1:
    print("There must be an odd number of lillypads.")
    raise SystemExit


def print_title():
    print(r"""
 _                       __                 
| |                     / _|                
| |     ___  __ _ _ __ | |_ _ __ ___   __ _ 
| |    / _ \/ _` | '_ \|  _| '__/ _ \ / _` |
| |___|  __/ (_| | |_) | | | | | (_) | (_| |
\_____/\___|\__,_| .__/|_| |_|  \___/ \__, |
                 | |                   __/ |
                 |_|                  |___/ 
""")


def print_board(board):
    print()
    print(" ".join(board))
    print(*range(NUM_LILLYPADS), sep=" ")
    print()


def init_board():
    board = []
    for i in range(NUM_LILLYPADS // 2):
        board.append(A)
    board.append(GAP)
    for i in range(NUM_LILLYPADS // 2):
        board.append(B)
    return board


def move(board, i):
    if can_hop(board, i) or can_leapfrog(board, i):
        j = board.index(GAP)
        board[i], board[j] = board[j], board[i]


def can_leapfrog(board, i):
    if i < 0 or i >= NUM_LILLYPADS:
        return False
    try:
        if board[i + 2] == GAP:
            return True
    except IndexError:
        pass
    try:
        if board[i - 2] == GAP:
            return True
    except IndexError:
        pass
    return False


def can_hop(board, i):
    if i < 0 or i >= NUM_LILLYPADS:
        return False
    try:
        if board[i + 1] == GAP:
            return True
    except IndexError:
        pass
    try:
        if board[i - 1] == GAP:
            return True
    except IndexError:
        pass
    return False


def is_legal_move(board, pos):
    return can_hop(board, pos) or can_leapfrog(board, pos)


def is_win(board, winning_board):
    return board == winning_board


def get_move():
    while True:
        try:
            position = int(input("Which froggie do you want to move (0-{})? ".format(NUM_LILLYPADS - 1)))
            if 0 <= position < NUM_LILLYPADS:
                return position
            else:
                print("That position is not valid. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def main():
    print_title()
    board = init_board()
    winning_board = board[::-1]
    moves_taken = 0
    print_board(board)
    while not is_win(board, winning_board):
        print("Turns taken: ", moves_taken)
        pos = get_move()
        if is_legal_move(board, pos):
            move(board, pos)
            moves_taken += 1
            print_board(board)
        else:
            print("No can do froggie.")
    print_board(board)
    print("Yay you won. It took {} moves".format(moves_taken))


if __name__ == "__main__":
    main()
