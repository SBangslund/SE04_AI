def minmax_decision(state):
    def max_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = -infinity
        for s in successors_of(state):
            v = max(v, min_value(s))
        print('V: ' + str(v))
        return v

    def min_value(state):
        if is_terminal(state):
            return utility_of(state)
        v = infinity
        for s in successors_of(state):
            v = min(v, max_value(s))
        return v

    infinity = float('inf')
    action = argmax(successors_of(state), lambda a: min_value(a))
    return action


def is_terminal(state):
    if state.count(1) == len(state):
        return True
    return False


def utility_of(state):
    if len(state) % 2 == 0:
        return -1
    return 1


def successors_of(state):
    successors = []
    for i in range(0, len(state)):
        if state[i] != 1:
            new_actions = []
            for j in range(1, int(state[i] / 2) + 1):
                new_actions.append([state[i] - j, j])
            updated_state = state.copy()
            updated_state.remove(state[i])
            for k in new_actions:
                k = k + updated_state
                if k not in successors:
                    successors.append(k)
    return successors


def argmax(iterable, func):
    return max(iterable, key=func)


def computer_select_pile(state):
    new_state = minmax_decision(state)
    return new_state


'''
Given a list of piles, asks the user to select a pile and then a split.
Then returns the new list of piles.
'''
def user_select_pile(list_of_piles):
    print("\n    Current piles: {}".format(list_of_piles))

    i = -1
    while i < 0 or i >= len(list_of_piles) or list_of_piles[i] < 3:
        print("Which pile (from 1 to {}, must be > 2)?".format(len(list_of_piles)))
        i = -1 + int(input())

    print("Selected pile {}".format(list_of_piles[i]))

    max_split = list_of_piles[i] - 1

    j = 0
    while j < 1 or j > max_split or j == list_of_piles[i] - j:
        if list_of_piles[i] % 2 == 0:
            print(
                'How much is the first split (from 1 to {}, but not {})?'.format(
                    max_split,
                    list_of_piles[i] // 2
                )
            )
        else:
            print(
                'How much is the first split (from 1 to {})?'.format(max_split)
            )
        j = int(input())

    k = list_of_piles[i] - j

    new_list_of_piles = list_of_piles[:i] + [j, k] + list_of_piles[i + 1:]

    print("    New piles: {}".format(new_list_of_piles))

    return new_list_of_piles


def main():
    state = [12]

    while not is_terminal(state):
        state = user_select_pile(state)
        if not is_terminal(state):
            state = computer_select_pile(state)

    print("    Final state is {}".format(state))


if __name__ == '__main__':
    main()
