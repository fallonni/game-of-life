import random
import os
import time


def main():
    inputs = print_initialisation()
    clear_terminal()
    if inputs[2]:
        board_state = load_from_file("toad.txt")
    else:
        board_state = create_random_board(*inputs[0])
    print_board_state(board_state)
    time.sleep(5)
    final_state = iterate_board(inputs[1], board_state)
    #print_board_state(final_state)


def print_initialisation():
    print("Welcome to the game of life....")
    load_file = input("Do you want to load your board from a file?").lower() != 'n'
    if load_file:
        iterations = int(input("How many iterations? "))
        print("Creating a Random world...")
        return (10, 10), iterations, load_file

    print("How large do you want your game?")
    x_size = int(input("What is the X dimension? "))
    y_size = int(input("What is the Y dimension? "))
    iterations = int(input("How many iterations? "))
    print("Creating a Random world...")
    return (x_size, y_size), iterations, load_file


def print_board_state(board):
    for row in board:
        for cell in row:
            print(print_cell(cell), end='')
        print("")


def print_cell(cell):
    if cell > 0:
        return u"\u25A0"
    return u"\u25A1"


def create_dead_board(x_size, y_size):
    board = [[0
              for _ in range(x_size)]
             for _ in range(y_size)]
    return board


def create_random_board(x_size, y_size):
    board = [[random.randint(0, 1)
              for _ in range(x_size)]
             for _ in range(y_size)]
    return board


def calculate_next_board_state(board):
    x_size = len(board[0])
    y_size = len(board)
    next_board = create_dead_board(x_size, y_size)

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            neighbours = count_neighbours(board, j, i)
            if neighbours == 2:
                next_board[i][j] = board[i][j]
            if neighbours == 3:
                next_board[i][j] =1
    return next_board


def count_neighbours(board, col, row):
    live_neighbours = 0
    for r in row-1, row, row+1:
        for c in col-1, col, col+1:
            if r == row and c == col:     #you can't be a neighbour to yourself
                continue
            if r < 0 or c < 0:    #Can't index out
                continue
            if c >= len(board[0]) or r >= len(board): #Can't index out
                continue
            live_neighbours += board[r][c]
    return live_neighbours


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def iterate_board(iterations, board):
    clear_terminal()
    for i in range(iterations):
        board = calculate_next_board_state(board)
        time.sleep(1)
        clear_terminal()
        print_board_state(board)
    return board

def load_from_file(filename):
    with open(filename) as file:
        return[[int(ch) for ch in line.strip()] for line in file]


if __name__ == '__main__':
    main()
