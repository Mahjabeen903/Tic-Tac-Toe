import random

# Function to print the game board
def print_board(board):
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check if the game is over
def check_win(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if there is a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Minimax algorithm to determine the best move
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI (O)
def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Function to play Tic-Tac-Toe with AI
def play_game():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', AI is 'X'.")
    print_board(board)

    # Game loop
    while True:
        # Player's move (human)
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] != " ":
            print("Cell already occupied! Try again.")
            continue

        board[row][col] = "O"
        print_board(board)

        # Check for win or draw
        if check_win(board, "O"):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI's turn...")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print(f"AI chose: {ai_move[0]}, {ai_move[1]}")
        print_board(board)

        # Check for win or draw
        if check_win(board, "X"):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
