'''
Modify your search-program to solve the following problem:
    A farmer has a goat, a cabbage and a wolf to move across a river with a boat
    that can only hold himself and one other passenger. If the goat and wolf are
    alone, the wolf will eat the goat. If the goat and cabbage are alone, the goat
    will eat the cabbage.

    Define the state-space for the problem. Hint. Use a tuple to represent the side
    of the river each is located; for example ('W', 'E', 'W', 'W') can represent the
    (farmer, wolf, goat, cabbage) locations. Use a list of tuples for the successor
    states. Include successor states that violate the problem constraints, that is
    ('W', 'W', 'E', 'E') which is the goat is alone with the cabbage; don't violate
    requirements that the boat can hold only two passengers (e.g all four passengers
    cannot move from one side to another at once, that is ('W', 'W', 'W', 'W') cannot
    become ('E', 'E', 'E', 'E')).

    Define successor_fn to return a list of states that do not violate the problem
    constraints.

    Results with depth first:
    fringe: [State: ('E', 'W', 'E', 'W') - Depth: 1]
    fringe: [State: ('W', 'W', 'E', 'W') - Depth: 2]
    fringe: [State: ('E', 'E', 'E', 'W') - Depth: 3, State: ('E', 'W', 'E', 'E') - Depth: 3]
    fringe: [State: ('E', 'E', 'E', 'W') - Depth: 3, State: ('W', 'W', 'E', 'E') - Depth: 4]
    fringe: [State: ('E', 'E', 'E', 'W') - Depth: 3, State: ('E', 'E', 'E', 'E') - Depth: 5]
    Solution path:
    State: ('E', 'E', 'E', 'E') - Depth: 5
    State: ('W', 'W', 'E', 'E') - Depth: 4
    State: ('E', 'W', 'E', 'E') - Depth: 3
    State: ('W', 'W', 'E', 'W') - Depth: 2
    State: ('E', 'W', 'E', 'W') - Depth: 1
    State: ('W', 'W', 'W', 'W') - Depth: 0

    Results with breadth first:
    fringe: [State: ('E', 'W', 'E', 'W') - Depth: 1]
    fringe: [State: ('W', 'W', 'E', 'W') - Depth: 2]
    fringe: [State: ('E', 'E', 'E', 'W') - Depth: 3, State: ('E', 'W', 'E', 'E') - Depth: 3]
    fringe: [State: ('E', 'W', 'E', 'E') - Depth: 3, State: ('W', 'E', 'E', 'W') - Depth: 4]
    fringe: [State: ('W', 'E', 'E', 'W') - Depth: 4, State: ('W', 'W', 'E', 'E') - Depth: 4]
    fringe: [State: ('W', 'W', 'E', 'E') - Depth: 4, State: ('E', 'E', 'E', 'E') - Depth: 5]
    fringe: [State: ('E', 'E', 'E', 'E') - Depth: 5, State: ('E', 'E', 'E', 'E') - Depth: 5]
    Solution path:
    State: ('E', 'E', 'E', 'E') - Depth: 5
    State: ('W', 'E', 'E', 'W') - Depth: 4
    State: ('E', 'E', 'E', 'W') - Depth: 3
    State: ('W', 'W', 'E', 'W') - Depth: 2
    State: ('E', 'W', 'E', 'W') - Depth: 1
    State: ('W', 'W', 'W', 'W') - Depth: 0
'''

w = 'W'
e = 'E'

INITIAL_STATE = (w, w, w, w)
GOAL_STATE = (e, e, e, e)
STATE_SPACE = {(w, w, w, w): [(e, w, w, e), (e, w, e, w), (e, e, w, w)],
               (e, w, w, e): [(w, w, w, e)],
               (e, w, e, w): [(w, w, e, w)],
               (e, e, w, w): [(w, e, w, w)],
               (w, w, w, e): [(e, e, w, e), (e, w, e, e)],
               (w, e, w, e): [(e, e, e, e)],
               (w, w, e, e): [(e, e, e, e)],
               (w, w, e, w): [(e, e, e, w), (e, w, e, e)],
               (w, e, e, w): [(e, e, e, e)],
               (e, w, e, e): [(w, w, e, e)],
               (w, e, w, w): [(e, e, e, w), (e, e, w, e)],
               (e, e, e, w): [(w, e, e, w)],
               (e, e, w, e): [(w, e, w, e)]
               }

last_state = INITIAL_STATE

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
        if node.STATE == GOAL_STATE:
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
    children = successor_fn(node.STATE)
    for child in children:
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
    q.reverse()
    node = q.pop()
    q.reverse()
    return node


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    global last_state
    impossible_states = [(e, w, w, e), (e, e, w, w)]
    approved_states = []

    for possible_state in STATE_SPACE[state]:
        if possible_state not in impossible_states:
            approved_states.append(possible_state)

    return approved_states  # successor_fn( 'C' ) returns ['F', 'G']


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
