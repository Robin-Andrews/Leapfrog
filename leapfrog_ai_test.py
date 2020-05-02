from leapfrog import *
import sys
import random


def test(did_pass):
    """Print the result of a test."""
    linenum = sys._getframe(1).f_lineno  # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def test_suite():
    """Run the suite of tests for code in this module (this file)."""
    # These tests assume a value of 7 for NUM_LILLYPADS
    board = init_board()
    test(board == [A, A, A, GAP, B, B, B])
    move(board, 2)
    test(board == [A, A, GAP, A, B, B, B])
    move(board, 4)
    test(board == [A, A, B, A, GAP, B, B])
    move(board, 6)
    test(board == [A, A, B, A, B, B, GAP])
    test(get_legal_moves(board) == [4, 5])
    test(can_hop(board, 7) is False)


def get_legal_moves(board):
    legal_moves = []
    gap_pos = board.index(GAP)
    for offset in [-2, -1, 1, 2]:
        potential_move_pos = gap_pos + offset
        if can_hop(board, potential_move_pos):
            legal_moves.append(potential_move_pos)
        if can_leapfrog(board, potential_move_pos):
            legal_moves.append(potential_move_pos)
    return legal_moves


def choose_random_legal_move(board):
    return random.choice(get_legal_moves(board))


def completely_random_play():
    board = init_board()
    winning_board = board[::-1]
    moves_taken = 0
    while not is_win(board, winning_board):
        moves_taken += 1
        move_pos = choose_random_legal_move(board)
        print_board(board)
        move(board, move_pos)
    print("AI won in {} moves.".format(moves_taken))


def monte_carlo():
    """Keep score of each move from a given position for many trials."""
    pass


def heuristic_play():
    """My first idea is to favour As moving right and Bs moving left."""
    pass


# test_suite()
completely_random_play()
