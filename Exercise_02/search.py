'''
1. Successor nodes are inserted at front of the fringe (successor list) as a
node is expanded. Is this a breadth (LIFO) or depth-first search (FIFO)?
    That would be a depth first as the newly explored nodes are then explored first.

2. For goal J, give the fringe (successor list) after expanding each node.
    fringe: [State: B - Depth: 1, State: C - Depth: 1]
    fringe: [State: B - Depth: 1, State: F - Depth: 2, State: G - Depth: 2]
    fringe: [State: B - Depth: 1, State: F - Depth: 2, State: H - Depth: 3, State: I - Depth: 3, State: J - Depth: 3]

3. What is the effect of inserting successor nodes at the end of the fringe as a
node is expanded? A depth or breadth-first search?
    That would be a breath-first search as newly explored nodes would get in the
    back of the fringe.

4. For goal J, give the fringe (successor list) after expanding each node.
    fringe: [State: B - Depth: 1, State: C - Depth: 1]
    fringe: [State: C - Depth: 1, State: D - Depth: 2, State: E - Depth: 2]
    fringe: [State: D - Depth: 2, State: E - Depth: 2, State: F - Depth: 2, State: G - Depth: 2]
    fringe: [State: E - Depth: 2, State: F - Depth: 2, State: G - Depth: 2]
    fringe: [State: F - Depth: 2, State: G - Depth: 2]
    fringe: [State: G - Depth: 2]
    fringe: [State: H - Depth: 3, State: I - Depth: 3, State: J - Depth: 3]
    fringe: [State: I - Depth: 3, State: J - Depth: 3]
    fringe: [State: J - Depth: 3]
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
    # for breadth first
    # q.reverse()
    # node = q.pop()
    # q.reverse()
    return q.pop()


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


INITIAL_STATE = 'A'
GOAL_STATE = 'J'
STATE_SPACE = {'A': ['B', 'C'],
               'B': ['D', 'E'],
               'C': ['F', 'G'],
               'D': [],
               'E': [],
               'F': [],
               'G': ['H', 'I', 'J'],
               'H': [],
               'I': [],
               'J': [], }

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
