import numpy as np

"""
Hidden Markov Model using Viterbi algorithm to find most
likely sequence of hidden states.

The problem is to find out the most likely sequence of states
of the weather (hot, cold) from a description of the number
of ice cream eaten by a boy in the summer.
"""


def main():
    np.set_printoptions(suppress=True)

    states = np.array(["initial", "hot", "cold", "final"])

    # To simulate starting from index 1, we add a dummy value at index 0
    observationss = [
        [None, 3, 1],
        [None, 3, 1, 3],
        [None, 3, 3, 1, 3],
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

        # path = compute_viterbi(states, observations, transitions, emissions)
        # print("Path: {}".format(' '.join(path)))

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
    return []


def argmax(sequence):
    # Note: You could use np.argmax(sequence), but only if sequence is a list.
    # If it is a generator, first convert it: np.argmax(list(sequence))
    return max(enumerate(sequence), key=lambda x: x[1])[0]


if __name__ == '__main__':
    main()
