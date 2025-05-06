import time
import copy

# Constants
X = "X"
O = "O"
EMPTY = " "

# Initial empty board
def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

# Get current player
def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count == o_count else O

# List of possible actions
def actions(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Resulting board after a move
def result(board, action, player_symbol):
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception("Invalid move")
    new_board = copy.deepcopy(board)
    new_board[i][j] = player_symbol
    return new_board

# Check for a winner
def winner(board):
    lines = board + [list(col) for col in zip(*board)]  # rows and columns
    lines.append([board[i][i] for i in range(3)])        # main diagonal
    lines.append([board[i][2 - i] for i in range(3)])    # anti-diagonal

    for line in lines:
        if line.count(X) == 3:
            return X
        if line.count(O) == 3:
            return O
    return None

# Check if the game is over
def terminal(board):
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)

# Utility of terminal state
def utility(board):
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0

# Minimax algorithm (used by X)
def minimax(board):
    if terminal(board):
        return None

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = float('-inf')
        best_action = None
        for action in actions(board):
            val, _ = min_value(result(board, action, X))
            if val > v:
                v = val
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = float('inf')
        best_action = None
        for action in actions(board):
            val, _ = max_value(result(board, action, O))
            if val < v:
                v = val
                best_action = action
        return v, best_action

    _, action = max_value(board) if player(board) == X else min_value(board)
    return action

# Alpha-Beta Pruning (used by O)
def alpha_beta(board):
    if terminal(board):
        return None

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = float('-inf')
        best_action = None
        for action in actions(board):
            val, _ = min_value(result(board, action, X), alpha, beta)
            if val > v:
                v = val
                best_action = action
            alpha = max(alpha, v)
            if beta <= alpha:
                break
        return v, best_action

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None
        v = float('inf')
        best_action = None
        for action in actions(board):
            val, _ = max_value(result(board, action, O), alpha, beta)
            if val < v:
                v = val
                best_action = action
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v, best_action

    _, action = max_value(board, float('-inf'), float('inf')) if player(board) == X else min_value(board, float('-inf'), float('inf'))
    return action

# Print the board
def print_board(board):
    for row in board:
        print(row)
    print()

# Main game loop
def play_game():
    board = initial_state()
    print("Initial board:")
    print_board(board)

    while not terminal(board):
        current = player(board)

        if current == X:
            start = time.time()
            move = minimax(board)
            end = time.time()
            print(f"Player X (Minimax) chooses: {move} (Time: {end - start:.4f}s)")
        else:
            start = time.time()
            move = alpha_beta(board)
            end = time.time()
            print(f"Player O (Alpha-Beta) chooses: {move} (Time: {end - start:.4f}s)")

        board = result(board, move, current)
        print_board(board)

    print("Game Over.")
    win = winner(board)
    if win:
        print(f"Winner: {win}")
    else:
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()

