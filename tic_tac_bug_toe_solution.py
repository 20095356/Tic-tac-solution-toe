# Fixed the win condition checks in the is_win function. Changed not all to all to properly check for winning conditions.
# Corrected the diagonal win condition in the is_win function. Changed board[1][0] to board[0][0].
# Added an explicit return False statement at the end of the is_win function to handle cases where no win condition is met.
# Wrapped the input reading in a try-except block to handle invalid input (e.g., non-integer input) gracefully.
# Added an except IndexError block to handle cases where the user enters row and column values outside the range (0-2).

"""A simple Tic-Tac-Toe game.

This script allows two players to play Tic-Tac-Toe against each other. The players take turns marking spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. If all spaces are filled without any player achieving a winning condition, the game ends in a draw.

Attributes:
    board (list): A 3x3 grid representing the game board.
    current_player (str): Indicates the current player, either 'X' or 'O'.
    moves (int): Tracks the number of moves made in the game.
    results (list): Stores the results of each game round, indicating whether a player has won or not.

Functions:
    print_board(): Prints the current state of the game board.
    is_win(player): Checks if the specified player has achieved a winning condition.
    tally_wins(results): Calculates the total number of wins based on the results list.
    main(): The main function to run the game loop and manage player interactions.

"""

board = [[' ' for _ in range(3)] for _ in range(3)]

def print_board():
    """Print the current state of the tic-tac-toe board"""
    for row in board:
        print('|'.join(row))
        print('-' * 5)

def is_win(board,player):
    '''Check rows, columns, and diagonals for win condition for a given player.
    A player wins if they have filled an entire row, column, or diagonal with their symbol.
    This function checks all rows, columns, and both diagonals to see if the player has won.
    Args:
    player (str): The symbol of the player ('X' or 'O').

    Returns:
    bool: True if the player has won, False otherwise.'''
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # 1. Changed 'not all' to 'all'
            return True
        if all([board[j][i] == player for j in range(3)]):  # 2. Changed 'not all' to 'all'
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:  # 3. Changed 'board[1][0]' to 'board[0][0]'
        return True
    return False  # 4. Added explicit return False if no win condition is met

def tally_wins(results):
    """Counts the number of wins in the results."""
    return sum(results)

def main():
    """The main function to run the Tic Tac Toe game.

    This function handles the game loop, player input, win checking, and game end conditions."""
    current_player = 'X'
    moves = 0
    results = []

    while moves < 9:
        print_board()
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2) separated by space: ").split())
            if board[row][col] == ' ':
                board[row][col] = current_player
                win = is_win(board,current_player)
                results.append(win)
                if win:
                    print_board()
                    print(f"Player {current_player} wins!")
                    return
                current_player = 'O' if current_player == 'X' else 'X'
                moves += 1
            else:
                print("Cell already occupied! Try again.")
        except ValueError:
            print("Invalid input! Please enter two integers separated by space.")
        except IndexError:
            print("Invalid input! Please enter row and column values within the range (0-2).")
    print_board()
    print("It's a draw!")
    print(f"Number of wins during the game: {tally_wins(results)}")

if __name__ == "__main__":
    main()
