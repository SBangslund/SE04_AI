'''
Use your search program to solve the vacuum world problem. Hint: one way
to represent the state space in Python is by a dictionary where the current
state is a tuple:
    (location, A status, B status) and a list hold successor states for each action:
        [(location, A status, B status), (location, A status, B status), (location, A status, B status)]

    for example:
    ('A', 'Dirty', 'Dirty'):
        [('A', 'Clean', 'Dirty'), ('A', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty')]

    Breath-first made the following results (preferable in this instance):
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('B', 'Dirty', 'Dirty') - Depth: 1]
        fringe: [State: ('B', 'Dirty', 'Dirty') - Depth: 1, State: ('B', 'Clean', 'Dirty') - Depth: 2]
        fringe: [State: ('B', 'Clean', 'Dirty') - Depth: 2, State: ('B', 'Dirty', 'Clean') - Depth: 2]
        fringe: [State: ('B', 'Dirty', 'Clean') - Depth: 2, State: ('B', 'Clean', 'Clean') - Depth: 3]
        fringe: [State: ('B', 'Clean', 'Clean') - Depth: 3, State: ('A', 'Dirty', 'Clean') - Depth: 3]
        Solution path:
        State: ('B', 'Clean', 'Clean') - Depth: 3
        State: ('B', 'Clean', 'Dirty') - Depth: 2
        State: ('A', 'Clean', 'Dirty') - Depth: 1
        State: ('A', 'Dirty', 'Dirty') - Depth: 0

    Depth-first made the following results:
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('B', 'Dirty', 'Dirty') - Depth: 1]
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('B', 'Dirty', 'Clean') - Depth: 2]
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('A', 'Dirty', 'Clean') - Depth: 3]
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('A', 'Clean', 'Clean') - Depth: 4]
        fringe: [State: ('A', 'Clean', 'Dirty') - Depth: 1, State: ('B', 'Clean', 'Clean') - Depth: 5]
        Solution path:
        State: ('B', 'Clean', 'Clean') - Depth: 5
        State: ('A', 'Clean', 'Clean') - Depth: 4
        State: ('A', 'Dirty', 'Clean') - Depth: 3
        State: ('B', 'Dirty', 'Clean') - Depth: 2
        State: ('B', 'Dirty', 'Dirty') - Depth: 1
        State: ('A', 'Dirty', 'Dirty') - Depth: 0
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
    # q.reverse()
    # node = q.pop()
    # q.reverse()
    return q.pop()


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = ('A', 'Dirty', 'Dirty')
GOAL_STATE = ('B', 'Clean', 'Clean')
STATE_SPACE = {('A', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty'), ('B', 'Dirty', 'Dirty')],
               ('A', 'Clean', 'Dirty'): [('B', 'Clean', 'Dirty')],
               ('B', 'Clean', 'Dirty'): [('B', 'Clean', 'Clean')],
               ('B', 'Dirty', 'Dirty'): [('B', 'Dirty', 'Clean')],
               ('B', 'Dirty', 'Clean'): [('A', 'Dirty', 'Clean')],
               ('A', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean')],
               ('A', 'Clean', 'Clean'): [('B', 'Clean', 'Clean')]}

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
