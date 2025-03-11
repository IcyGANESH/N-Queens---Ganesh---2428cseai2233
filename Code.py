import random  # Importing random module to generate random numbers

# Function to print the chessboard
def print_board(board):
    for row in range(len(board)):
        line = ''
        for col in range(len(board)):
            if board[row] == col:
                line += 'Q '  # Placing a Queen (Q)
            else:
                line += '. '  # Empty space
        print(line)  # Print each row
    print()

# Function to count conflicts for each queen
def get_conflicts(board):
    conflicts = [0] * len(board)  # Initialize conflict list
    for i in range(len(board)):
        for j in range(len(board)):
            if i != j:
                # Checking if queens attack each other in the same column or diagonals
                if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                    conflicts[i] += 1
    return conflicts  # Return conflict counts

# Hill climbing algorithm to reduce conflicts
def hill_climb(board):
    while True:
        conflicts = get_conflicts(board)  # Get conflict list
        max_conflict = max(conflicts)  # Find max conflicts

        if max_conflict == 0:
            return board  # If no conflicts, return solution

        # Get all indexes with maximum conflict
        max_conflict_indexes = [i for i in range(len(board)) if conflicts[i] == max_conflict]
        queen_to_move = random.choice(max_conflict_indexes)  # Pick a random queen with max conflict

        best_position = board[queen_to_move]  # Store current position
        min_conflict = conflicts[queen_to_move]  # Store current conflicts

        for col in range(len(board)):
            if col != board[queen_to_move]:
                temp_board = board[:]  # Create a temporary board
                temp_board[queen_to_move] = col  # Move queen to new column
                temp_conflicts = get_conflicts(temp_board)  # Get new conflicts

                if temp_conflicts[queen_to_move] < min_conflict:  # If conflict reduces
                    min_conflict = temp_conflicts[queen_to_move]  # Update min conflict
                    best_position = col  # Update best position

        board[queen_to_move] = best_position  # Move queen to best position

        # If no improvement, restart with a new random board
        if min_conflict == conflicts[queen_to_move]:
            board = [random.randint(0, len(board)-1) for _ in range(len(board))]

    return board  # Return final board

# Function to solve the N-Queens problem
def solve_n_queens(n):
    board = [random.randint(0, n-1) for _ in range(n)]  # Randomly place queens
    return hill_climb(board)  # Solve using hill climbing

# Taking user input for the number of queens
n = int(input("Enter the number of queens: "))
solution = solve_n_queens(n)  # Solve the problem
print("Solution:")
print_board(solution)  # Print the final board
