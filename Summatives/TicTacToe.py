

def print_board(board):
    # Print the current state of the Tic-Tac-Toe board
    print("\nCurrent board:")
    for i in range(3):
        print(" " + board[i*3] + " | " + board[i*3+1] + " | " + board[i*3+2])
        if i != 2:
            print("-----------")

def check_winner(board):
    # Check for a winner on the current board
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def is_board_full(board):
    # Check if the board is full
    return all(cell != " " for cell in board)

def play_game():
    # function to play a single game
    board = [" " for _ in range(9)]
    player = "X"

    while True:
        print_board(board)
        try:
            position = int(input(f"Player {player}, enter a position (1-9): ")) - 1
            if not 0 <= position <= 8 or board[position] != " ":
                print("Invalid position. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        board[position] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

def main():
    # Main function to start the game ask to play again
    while True:
        play_game()
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            break

main()
