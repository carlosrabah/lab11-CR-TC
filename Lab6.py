def initialize_board(num_rows, num_cols):
    board = []
    for _ in range(num_rows):
        board.append(["-"] * num_cols)
    return board

def print_board(board):
    for row in board:
        print(*row)

def insert_chip(board, col, chip_type):
    num_rows = len(board)
    for x in range(num_rows - 1, -1, -1):
        if board[x][col] == "-":
            board[x][col] = chip_type
            print_board(board)
            return x
    return None

def check_if_winner(board, col, row, chip_type):
    num_rows = len(board)
    num_cols = len(board[0])

    count = 0
    for x in range(num_rows):
        if board[x][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    count = 0
    for y in range(num_cols):
        if board[row][y] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False


if __name__ == "__main__":
    i = 1
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print("Player 1: x \nPlayer 2: o")

    while True:
        col = int(input(f"Player {i}: Which column would you like to choose? "))
        if col < 0 or col >= num_cols:
            print("Invalid column. Try again.")
            continue

        chip_type = "x" if i == 1 else "o"
        row = insert_chip(board, col, chip_type)
        if row is None:
            print("That column is full. Choose another.")
            continue

        if check_if_winner(board, col, row, chip_type):
            if chip_type == "x":
                print("Player 1 won the game!")
            else:
                print("Player 2 won the game!")
            break

        full = True
        for r in board:
            if "-" in r:
                full = False
                break
        if full:
            print("Draw. Nobody wins.")
            break

        i = 2 if i == 1 else 1