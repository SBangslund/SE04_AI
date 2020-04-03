def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for (a, s) in successors_of(state):
            v = max(v, min_value(s))
        #print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for (a, s) in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action, state = argmax(successors_of(state), lambda a: min_value(a[1]))
    return action


'''
returns True if the state is either a win or a tie (board full)
:param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
:return:
'''
def is_terminal(state):
    if state.count('X') >= 3 and check_character_for_terminal(state, 'X'):
        return True

    if state.count('O') >= 3 and check_character_for_terminal(state, 'O'):
        return True

    if state.count('X') + state.count('O') >= len(state):
        return True

    return False


def check_character_for_terminal(state, character):
    checked_character = [i for i in range(0, 9) if state[i] == character]
    check_table = {
        0: [0, 4, 8],  # diagonal 1
        1: [2, 4, 6],  # diagonal 2
        2: [0, 1, 2],  # side 1
        3: [0, 3, 6],  # side 2
        4: [6, 7, 8],  # side 3
        5: [2, 5, 8],  # side 4
        6: [3, 4, 5],  # middle 1
        7: [1, 4, 7]   # middle 2
    }
    for i in range(0, len(check_table)):
        if len([value for value in check_table[i] if value in checked_character]) == 3:
            return True
    return False


'''
returns +1 if winner is X (MAX player), -1 if winner is O (MIN player), or 0 otherwise
:param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
:return:
'''
def utility_of(state):
    if check_character_for_terminal(state, 'X'):
        return 1

    if check_character_for_terminal(state, 'O'):
        return -1

    return 0


'''
returns a list of tuples (move, state) as shown in the exercise slides
:param state: State of the checkerboard. Ex: [0; 1; 2; 3; X; 5; 6; 7; 8]
:return:
'''
def successors_of(state):
    possible_moves = []
    for state_index in range(0, 9):
        if state[state_index] != 'X' and state[state_index] != 'O':
            moves_list = []
            for i in range(0, 9):
                if i == state_index and state.count('X') == state.count('O'):
                    moves_list.append('X')
                elif i == state_index and state.count('X') > state.count('O'):
                    moves_list.append('O')
                else:
                    moves_list.append(state[i])
            possible_moves.append((state_index, moves_list.copy()))
    return possible_moves


def display(state):
    print("-----")
    for c in [0, 3, 6]:
        print(state[c + 0], state[c + 1], state[c + 2])


def main():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    while not is_terminal(board):
        board[minmax_decision(board)] = 'X'
        if not is_terminal(board):
            display(board)
            board[int(input('Your move? '))] = 'O'
    display(board)


def argmax(iterable, func):
    return max(iterable, key=func)


if __name__ == '__main__':
    main()
