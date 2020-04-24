'''
1. Run the module.
2. Enter: run(10)
    Current                    New
    location   status  action  location  status
    A          Dirty   Suck    A         Clean
    A          Clean   Right   B         Dirty
    B          Dirty   Suck    B         Clean
    B          Clean   Left    A         Clean
    A          Clean   Right   B         Clean
    B          Clean   Left    A         Clean
    A          Clean   Right   B         Clean
    B          Clean   Left    A         Clean
    A          Clean   Right   B         Clean

3. Change the SIMPLE_REFLEX_AGENT condition action rules to return bogus actions, such as Left when
should go Right, or Crash, etc. Rerun the agent. Do the Actuators allow bogus actions?
    Don't really understand what is meant by this question but I have added support for
    the NoOp rule.
    Current                    New
    location   status  action  location  status
    A          Dirty   Suck    A         Clean
    A          Clean   Right   B         Dirty
    B          Dirty   Suck    B         Clean
    B          Clean   NoOp    B         Clean
    B          Clean   NoOp    B         Clean
    B          Clean   NoOp    B         Clean
    B          Clean   NoOp    B         Clean
    B          Clean   NoOp    B         Clean
    B          Clean   NoOp    B         Clean

Extend the REFLEX-AGENT-WITH-STATE program to
have 4 locations (4 squares):
• The agent should only sense and act on the square where it is
located.
• Allow any starting square.
• Use run (20) to test and display results.
    Current                    New
    location   status  action  location  status
    C          Dirty   Suck    C         Clean
    C          Clean   Left    D         Dirty
    D          Dirty   Suck    D         Clean
    D          Clean   Up      A         Dirty
    A          Dirty   Suck    A         Clean
    A          Clean   Right   B         Dirty
    B          Dirty   Suck    B         Clean
    B          Clean   Down    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
    C          Clean   NoOp    C         Clean
'''

A = 'A'
B = 'B'
C = 'C'
D = 'D'

state = {}
action = None
model = {A: None, B: None, C: None, D: None}  # Initially ignorant

rule_action = {
    1: 'Suck',
    2: 'Right',
    3: 'Down',
    4: 'Left',
    5: 'Up',
    6: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (C, 'Dirty'): 1,
    (D, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (C, 'Clean'): 4,
    (D, 'Clean'): 5,
    (A, B, C, D, 'Clean'): 6
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    C: 'Dirty',
    D: 'Dirty',
    'Current': C
}


def reflex_agent_with_state(percept):  # Determine action
    global state, action
    state = update_state(state, action, percept)
    rule = rule_match(state, rules)
    action = rule_action[rule]
    return action


def update_state(state, action, percept):
    (location, status) = percept
    state = percept
    if model[A] == model[B] == model[C] == model[D] == 'Clean':
        state = (A, B, C, D, 'Clean')
    model[location] = status
    return state


def interpret_input(input):  # No interpretation
    return input


def rule_match(state, rules):  # Match rule for a given state
    rule = rules.get(tuple(state))
    return rule


def sensors():  # Sense environment
    location = environment['Current']
    return (location, environment[location])


def actuators(action):  # Modify environment
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B  # Move to B
    elif action == 'Down' and location == B:
        environment['Current'] = C  # Move to C
    elif action == 'Left' and location == C:
        environment['Current'] = D  # Move to D
    elif action == 'Up' and location == D:
        environment['Current'] = A  # Move to A


def run(n):  # Run the agent through n steps
    print('Current                    New')
    print('location   status  action  location  status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:11s}{:8s}".format(location, status), end='')
        action = reflex_agent_with_state(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:10s}{:8s}".format(action, location, status))


run(20)
