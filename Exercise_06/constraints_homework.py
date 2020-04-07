'''
Modify the program form the exercise to use:
    - The map of South America on the last slide
    - 4 colors (red, green, blue and yellow)

Output:
    Argentina: Yellow
    Bolivia: Green
    Brazil: Red
    Chile: Red
    Colombia: Green
    Costa Rica: Green
    Ecuador: Red
    Guyana: Green
    Guyana (Fr): Green
    Panama: Red
    Paraguay: Blue
    Peru: Blue
    Suriname: Blue
    Uruguay: Green
    Venezuela: Blue
'''


class CSP:
    def __init__(self, variables, domains, neighbours, constraints):
        self.variables = variables
        self.domains = domains
        self.neighbours = neighbours
        self.constraints = constraints

    def backtracking_search(self):
        return self.recursive_backtracking({})

    def recursive_backtracking(self, assignment):
        if self.is_complete(assignment):
            return assignment
        var = self.select_unassigned_variable(assignment)
        for value in self.order_domain_values(var, assignment):
            if self.is_consistent(var, value, assignment):
                assignment[var] = value
                result = self.recursive_backtracking(assignment)
                if result is not None:
                    return result
                assignment.pop(var)
        return None

    def select_unassigned_variable(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return variable

    def is_complete(self, assignment):
        for variable in self.variables:
            if variable not in assignment:
                return False
        return True

    def order_domain_values(self, variable, assignment):
        all_values = self.domains[variable][:]
        # shuffle(all_values)
        return all_values

    def is_consistent(self, variable, value, assignment):
        if not assignment:
            return True

        for constraint in self.constraints.values():
            for neighbour in self.neighbours[variable]:
                if neighbour not in assignment:
                    continue

                neighbour_value = assignment[neighbour]
                if not constraint(variable, value, neighbour, neighbour_value):
                    return False
        return True


def create_australia_csp():
    br, bo, pa, ar, ur, ch, pe, ec, co, ve, gu1, su, gu2, pan, cr = 'Brazil', 'Bolivia', 'Paraguay', 'Argentina', 'Uruguay', 'Chile', 'Peru', 'Ecuador', 'Colombia', 'Venezuela', 'Guyana', 'Suriname', 'Guyana (Fr)', 'Panama', 'Costa Rica'
    values = ['Red', 'Green', 'Blue', 'Yellow']
    variables = [br, bo, pa, ar, ur, ch, pe, ec, co, ve, gu1, su, gu2, pan, cr]
    domains = {
        br: values[:],
        bo: values[:],
        pa: values[:],
        ar: values[:],
        ur: values[:],
        ch: values[:],
        pe: values[:],
        ec: values[:],
        co: values[:],
        ve: values[:],
        gu1: values[:],
        gu2: values[:],
        su: values[:],
        pan: values[:],
        cr: values[:]
    }
    neighbours = {
        br: [ur, pa, bo, pe, co, ve, gu1, gu2, su],
        bo: [pa, pe, br, ch, ar],
        pa: [ar, ur, bo, br],
        ar: [ch, ur, pa, bo, br],
        ur: [ar, br],
        ch: [ar, bo, pe],
        pe: [ch, bo, br, ec, co],
        ec: [pe, co],
        co: [ec, pe, ve, br, pan],
        ve: [co, gu1, br],
        gu1: [ve, su, br],
        su: [gu1, gu2, br],
        gu2: [su, br],
        pan: [cr, co],
        cr: [pan]
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        br: constraint_function,
        bo: constraint_function,
        pa: constraint_function,
        ar: constraint_function,
        ur: constraint_function,
        ch: constraint_function,
        pe: constraint_function,
        ec: constraint_function,
        co: constraint_function,
        ve: constraint_function,
        gu1: constraint_function,
        su: constraint_function,
        gu2: constraint_function,
        pan: constraint_function,
        cr: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
