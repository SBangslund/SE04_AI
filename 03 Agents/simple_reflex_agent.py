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
'''

A = 'A'
B = 'B'

rule_action = {
    1: 'Suck',
    2: 'Right',
    3: 'Left',
    4: 'NoOp'
}

rules = {
    (A, 'Dirty'): 1,
    (B, 'Dirty'): 1,
    (A, 'Clean'): 2,
    (B, 'Clean'): 3,
    (A, B, 'Clean'): 4
}

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def simple_reflex_agent(percept):  # Determine action
    state = interpret_input(percept)
    rule = rule_match(state, rules)
    action = rule_action[rule]
    return action


def interpret_input(input):  # No interpretation
    return input


def rule_match(state, rules):  # Match rule for a given state
    rule = rules.get(tuple(state))

    if environment[A] == 'Clean' and environment[B] == 'Clean':
        rule = 4

    return rule


def sensors():  # Sense environment
    location = environment['Current']
    return (location, environment[location])


def actuators(action):  # Modify environment
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'
    elif action == 'Right' and location == A:
        environment['Current'] = B
    elif action == 'Left' and location == B:
        environment['Current'] = A


def run(n):  # Run the agent through n steps
    print('Current                    New')
    print('location   status  action  location  status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:11s}{:8s}".format(location, status), end='')
        action = simple_reflex_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:10s}{:8s}".format(action, location, status))


run(10)
