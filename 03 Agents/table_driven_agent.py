'''
1. Run the module (using run()).
    Action	Percepts
    Right 	 [('A', 'Clean')]
    Suck 	 [('A', 'Clean'), ('A', 'Dirty')]
    Left 	 [('A', 'Clean'), ('A', 'Dirty'), ('B', 'Clean')]

2. The percepts should now be: [('A', 'Clean'), ('A', 'Dirty'), ('B',
'Clean')].
    – The table contains all possible percept sequences to match with the
    percept history.
    – Enter:
        print (TABLE_DRIVEN_AGENT((B, 'Clean'))) percepts
    – Explain the results.
        No idea what you mean?

3. How many table entries would be required if only the current
percept was used to select an action rather than the percept
history?
    Since there is only 4 relevant states (A, 'Clean'): Right, (B, 'Clean): Left,
    (A, 'Dirty'): Suck, (B, 'Dirty'): Suck, the table would contain 4 tuples.

4. How many table entries are required for an agent lifetime of T
steps?
    4^T.
'''


A = 'A'
B = 'B'

percepts = []
table = {
    ((A, 'Clean'),): 'Right',
    ((A, 'Dirty'),): 'Suck',
    ((B, 'Clean'),): 'Left',
    ((B, 'Dirty'),): 'Suck',
    # ...
    ((A, 'Clean'), (A, 'Dirty')): 'Suck',
    # ...
    ((A, 'Clean'), (A, 'Dirty'), (B, 'Clean')): 'Left'
}


def lookup(percepts, table):    # Find action based on percepts
    return table.get(tuple(percepts))


def table_driven_agent(percept):   # Determine action based on table and percepts
    percepts.append(percept)       # Add percepts
    return lookup(percepts, table)  # Lookup appropriate action for percepts


def run():  # Run agent on several sequential percepts
    print('Action\tPercepts')
    print(table_driven_agent((A, 'Clean')), '\t', percepts)
    print(table_driven_agent((A, 'Dirty')), '\t', percepts)
    print(table_driven_agent((B, 'Clean')), '\t', percepts)

run()

