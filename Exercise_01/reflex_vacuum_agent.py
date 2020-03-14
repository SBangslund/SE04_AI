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

3. Should bogus actions be able to corrupt the environment? Change the REFLEX_VACUUM_AGENT
to return bogus actions, such as Left when should go Right, etc. Run the agent. Do the
Actuators allow bogus actions?
    Not sure what is meant by allow? The logic will just make it go towards left indefinitely
    which in a real world scenario would be bad (and thus should not be allowed). In that case
    yes, the actuators allows bogus actions.
    Current                    New
    location   status  action  location  status
    A          Dirty   Suck    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
    A          Clean   Left    A         Clean
'''

A = 'A'
B = 'B'

environment = {
    A: 'Dirty',
    B: 'Dirty',
    'Current': A
}


def reflex_vacuum_agent(location_state):  # Determine action
    if location_state[1] == 'Dirty':
        return 'Suck'
    if location_state[0] == A:
        return 'Left'
    if location_state[0] == B:
        return 'Right'


def sensors():  # Sense environment
    location = environment['Current']  # Is it at A or B
    return (location, environment[location])  # Returns the state of its current location


def actuators(action):  # Modify environment
    location = environment['Current']
    if action == 'Suck':
        environment[location] = 'Clean'  # Clean current location
    elif action == 'Right' and location == A:
        environment['Current'] = B  # Move to B
    elif action == 'Left' and location == B:
        environment['Current'] = A  # Move to A


def run(n):  # Run the agent through n steps
    print('Current                    New')
    print('location   status  action  location  status')
    for i in range(1, n):
        (location, status) = sensors()
        print("{:11s}{:8s}".format(location, status), end='')
        action = reflex_vacuum_agent(sensors())
        actuators(action)
        (location, status) = sensors()
        print("{:8s}{:10s}{:8s}".format(action, location, status))


run(10)
