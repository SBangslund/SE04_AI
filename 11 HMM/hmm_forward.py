import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a description of the number
of ice cream eaten by a boy in the summer.

output:
    Observations: 3 3 1 1 2 2 3 1 3
    Probability: 1.5832347513504005e-06
    Path: hot hot hot hot hot cold cold hot hot
    
    Observations: 3 3 1 1 2 3 3 1 2
    Probability: 1.7262432888480009e-06
    Path: cold cold hot hot hot cold cold hot hot
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 3, 1, 1, 2, 2, 3, 1, 3],
        [None, 3, 3, 1, 1, 2, 3, 3, 1, 2],
    ]

    # Markov transition matrix
    # transitions[start, end]
    transitions = np.array([[.0, .8, .2, .0],  # Initial state
                            [.0, .6, .3, .1],  # Hot state
                            [.0, .4, .5, .1],  # Cold state
                            [.0, .0, .0, .0],  # Final state
                            ])

    # P(v|q)
    # emission[state, observation]
    emissions = np.array([[.0, .0, .0, .0],  # Initial state
                          [.0, .2, .4, .4],  # Hot state
                          [.0, .5, .4, .1],  # Cold state
                          [.0, .0, .0, .0],  # Final state
                          ])

    for observations in observationss:
        print("Observations: {}".format(' '.join(map(str, observations[1:]))))

        probability = compute_forward(states, observations, transitions, emissions)
        print("Probability: {}".format(probability))

        path = compute_viterbi(states, observations, transitions, emissions)
        print("Path: {}".format(' '.join(path)))

        print('')


def inclusive_range(a, b):
    return range(a, b + 1)


def compute_forward(states, observations, transitions, emissions):
    N = len(states)
    T = len(observations)
    qf = N - 1

    forward = np.empty([N + 2, T])
    for s in range(1, N):
        forward[s, 1] = transitions[0, s] * emissions[s, observations[1]]
    for t in range(2, T):
        for s in range(1, N):
            sum = 0
            for s2 in range(1, N):
                sum += forward[s2, t - 1] * transitions[s2, s] * emissions[s, observations[t]]
            forward[s, t] = sum
    sum = 0
    for s in range(1, N):
        sum += forward[s, T - 1] * transitions[s, qf]
    forward[qf, T - 1] = sum
    return forward[qf, T - 1]


def compute_viterbi(states, observations, transitions, emissions):
    N = len(states)
    T = len(observations)
    qf = N - 1

    viterbi = np.empty([N + 2, T])
    backpointer = np.empty([N, T])

    for s in range(1, N):
        viterbi[s, 1] = transitions[0, s] * emissions[s, observations[1]]
        backpointer[s, 1] = 0
    for t in range(2, T):
        for s in range(1, N):
            max_list = []
            argmax_list = []
            for s2 in range(1, N):
                max_list.append(viterbi[s2, t - 1] * transitions[s2, s] * emissions[s, observations[t]])
                argmax_list.append(viterbi[s2, t - 1] * transitions[s2, s])
            viterbi[s, t] = max(max_list)
            backpointer[s, t] = int(argmax(argmax_list))

    max_list = []
    argmax_list = []
    for s in range(1, N):
        max_list.append(viterbi[s, T - 1] * transitions[s, qf])
        argmax_list.append(viterbi[s, T - 1] * transitions[s, qf])
    viterbi[qf, T - 1] = max(max_list)
    backpointer[qf, T - 1] = int(argmax(argmax_list))

    trace = []
    next_index = int(backpointer[qf, T - 1])
    for i in range(T - 1, 0, -1):
        trace.append(states[next_index + 1])
        next_index = int(backpointer[next_index + 1, i])
    return trace


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))
    return max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
