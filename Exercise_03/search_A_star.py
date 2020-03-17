'''
Modify the program from last class to implement the greedy best first and
A* search for this graph. Compare solution paths. Play with the heuristics
and see what different heuristic functions would yield as solutions.

Play with weighted A* with different weights, and compare.

2. A*
    fringe: [State: ('B', 1, 5) - Depth: 1]
    fringe: [State: ('E', 4, 4) - Depth: 2]
    fringe: [State: ('H', 3, 1) - Depth: 3]
    fringe: [State: ('L', 5, 0) - Depth: 4]
    Solution path:
    State: ('L', 5, 0) - Depth: 4
    State: ('H', 3, 1) - Depth: 3
    State: ('E', 4, 4) - Depth: 2
    State: ('B', 1, 5) - Depth: 1
    State: ('A', 0, 6) - Depth: 0


'''


class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def tree_search():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = insert(initial_node, fringe)
    while fringe is not None:
        node = remove_first(fringe)
        if node.STATE in GOAL_STATE:
            return node.path()
        children = expand(node)
        fringe = insert_all(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def expand(node):
    successors = []
    child = successor_fn(node.STATE)
    #for child in children:
    s = Node(node)  # create node for each in state list
    s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
    s.PARENT_NODE = node
    s.DEPTH = node.DEPTH + 1
    successors = insert(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def insert(node, q):
    q.append(node)
    return q


'''
Insert list of nodes into the fringe
'''


def insert_all(l, q):
    for i in range(0, len(l)):
        q.append(l[i])
    return q


'''
Removes and returns the first element from fringe
'''


def remove_first(q):
    # for breadth first
    # q.reverse()
    # node = q.pop()
    # q.reverse()
    return q.pop()


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    possible_states = STATE_SPACE[state]
    heuristics = []
    for i in range(0, len(possible_states)):
        heuristics.append(possible_states[i][1] + possible_states[i][2])

    minimum_heuristic = 0
    for i in range(0, len(heuristics)):
        if heuristics[minimum_heuristic] > heuristics[i]:
            minimum_heuristic = i
    return possible_states[minimum_heuristic]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 0, 6)
GOAL_STATE = [('K', 6, 0), ('L', 5, 0), ('L', 3, 0)]
STATE_SPACE = {('A', 0, 6): [('B', 1, 5), ('C', 2, 5), ('D', 4, 2)],
               ('B', 1, 5): [('F', 5, 5), ('E', 4, 4)],
               ('C', 2, 5): [('E', 1, 4)],
               ('D', 4, 2): [('H', 1, 1), ('I', 4, 2), ('J', 2, 1)],
               ('E', 4, 4): [('G', 2, 4), ('H', 3, 1)],
               ('E', 1, 4): [('G', 2, 4), ('H', 3, 1)],
               ('F', 5, 5): [('G', 1, 4)],
               ('G', 1, 4): [('K', 6, 0)],
               ('G', 2, 4): [('K', 6, 0)],
               ('H', 3, 1): [('K', 6, 0), ('L', 5, 0)],
               ('H', 1, 1): [('K', 6, 0), ('L', 5, 0)],
               ('I', 4, 2): [('L', 3, 0)],
               ('J', 2, 1): [],
               ('K', 6, 0): [],
               ('L', 5, 0): [],
               ('L', 3, 0): []
               }


'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = tree_search()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()
