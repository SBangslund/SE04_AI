"""
Chessboard module

"""


def fitness_fn_negative(individual):
    '''
    Compute the number of conflicting pairs, negated.
    For a solution with 5 conflicting pairs the return value is -5, so it can
    be maximized to 0.
    '''

    n = len(individual)
    fitness = 0
    for column, row in enumerate(individual):
        contribution = 0

        # Horizontal
        for other_column in range(column + 1, n):
            if individual[other_column] == row:
                contribution += 1

        # Diagonals
        for other_column in range(column + 1, n):
            row_a = row + (column - other_column)
            row_b = row - (column - other_column)
            if 0 <= row_a < n and individual[other_column] == row_a:
                contribution += 1
            if 0 <= row_b < n and individual[other_column] == row_b:
                contribution += 1

        fitness += contribution

    return - fitness


def fitness_fn_positive(state):
    '''
    Compute the number of non-conflicting pairs.
    '''

    def conflicted(state, row, col):
        for c in range(col):
            if conflict(row, col, state[c], c):
                return True

        return False

    def conflict(row1, col1, row2, col2):
        return (
            row1 == row2 or
            col1 == col2 or
            row1 - col1 == row2 - col2 or
            row1 + col1 == row2 + col2
        )

    fitness = 0
    for col in range(len(state)):
        for pair in range(1, col + 1):
            if not conflicted(state, state[pair], pair):
                fitness = fitness + 1
    return fitness
