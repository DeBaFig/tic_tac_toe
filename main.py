import math


def create_board():
    """Initializes the 3x3 Tic-Tac-Toe board."""
    return [' ' for _ in range(9)]


def display_board(board):
    """Prints the board to the console."""
    print('-------------')
    for i in range(3):
        print(f'| {board[i*3]} | {board[i*3 + 1]} | {board[i*3 + 2]} |')
        print('-------------')


def check_win(board, player):
    """Checks all winning combinations (rows, columns, diagonals)."""
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(
        all(board[i] == player for i in combo)
        for combo in win_conditions
    )


def is_board_full(board):
    """Checks if the board is completely filled (a draw)."""
    return ' ' not in board


def get_available_moves(board):
    """Returns a list of indices of empty cells."""
    return [i for i, spot in enumerate(board) if spot == ' ']


SCORE_MAP = {'X': 1, 'O': -1, 'draw': 0}


def minimax(board, depth, is_maximizing_player):
    """
    The Minimax algorithm function.
    It recursively evaluates the board and returns the best score.
    """

    if check_win(board, 'X'):
        return SCORE_MAP['X'] - depth
    if check_win(board, 'O'):
        return SCORE_MAP['O'] + depth
    if is_board_full(board):
        return SCORE_MAP['draw']

    if is_maximizing_player:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = min(best_score, score)
        return best_score


def find_best_move(board):
    """
    Iterates through all possible moves and uses minimax
    to find the move that leads to the highest score.
    """
    best_score = -math.inf
    best_move = -1

    for move in get_available_moves(board):
        board[move] = 'X'
        score = minimax(board, 0, False)

        board[move] = ' '

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


def play_game():
    """Main function to run the Tic-Tac-Toe game."""
    board = create_board()
    human_player = 'O'
    ai_player = 'X'
    current_player = human_player

    print("Welcome to Tic-Tac-Toe! You are 'O', the AI is 'X'.")
    print("The board positions correspond to numbers 0-8:")
    print("0 | 1 | 2")
    print("---------")
    print("3 | 4 | 5")
    print("---------")
    print("6 | 7 | 8\n")

    display_board(board)

    while (not is_board_full(board) and
           not check_win(board, human_player) and
           not check_win(board, ai_player)):

        if current_player == human_player:
            try:
                move = int(input(
                    f"Your turn ({human_player}). Enter a move (0-8): "))
                if move in range(9) and board[move] == ' ':
                    board[move] = human_player
                    current_player = ai_player
                else:
                    print("Invalid move. Please choose an empty cell (0-8).")
                    continue
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        else:
            print("AI is thinking...")
            ai_move = find_best_move(board)
            if ai_move != -1:
                board[ai_move] = ai_player
                print(f"AI chose position {ai_move}")
                current_player = human_player

        display_board(board)

    if check_win(board, human_player):
        print("🎉 Congratulations! You win!")
    elif check_win(board, ai_player):
        print("🤖 AI wins! Better luck next time.")
    else:
        print("🤝 It's a draw!")


if __name__ == '__main__':
    play_game()
