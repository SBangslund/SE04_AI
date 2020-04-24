'''
1. What is returned by create_australia_csp()?
    An instance of the CSP class with preset values, variables, domains and neighbors.

2. What is returned by backtracking_search()?
    A dictionary of the different variables and their assigned values (in accordance with
    their constraints). This uses the recursive backtracking search.

3. What is the purpose of the assignment variable?
    The assignment variable is the variable holding the currently assigned values. These are
    then evaluated against constraints to achieve a better assignment (recursively).

4. What is the purpose of the variable variable?
    I am guessing this is the var variable in the recursive_backtracking_search(). This is
    set to an unassigned variable currently available in the assignments. Continuing on, this
    is used to assign a value from the domain.

5. What is the purpose of the following statement?
    for value in the self.order_domain_values(variable, assignment)
    Iterates through the different values available in the domain ([Red, Blue, Green]).

6. What would the following do?
    if self.is_consistent('Q': 'Red', 'NT': 'Blue', 'NSW': 'green'):
        assignment[variable] = value
    Makes sure to only assign the value to a variable if the currently stored values are
    consistent with the constraints.

7. What would then assignment be?
    (Is this the same question as 3?). I am not sure what to answer here.

8. What is the effect of del assignment[variable]?
     Deletes the list of current assignments.
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
    wa, q, t, v, sa, nt, nsw = 'WA', 'Q', 'T', 'V', 'SA', 'NT', 'NSW'
    values = ['Red', 'Green', 'Blue']
    variables = [wa, q, t, v, sa, nt, nsw]
    domains = {
        wa: values[:],
        q: values[:],
        t: values[:],
        v: values[:],
        sa: values[:],
        nt: values[:],
        nsw: values[:],
    }
    neighbours = {
        wa: [sa, nt],
        q: [sa, nt, nsw],
        t: [],
        v: [sa, nsw],
        sa: [wa, nt, q, nsw, v],
        nt: [sa, wa, q],
        nsw: [sa, q, v],
    }

    def constraint_function(first_variable, first_value, second_variable, second_value):
        return first_value != second_value

    constraints = {
        wa: constraint_function,
        q: constraint_function,
        t: constraint_function,
        v: constraint_function,
        sa: constraint_function,
        nt: constraint_function,
        nsw: constraint_function,
    }

    return CSP(variables, domains, neighbours, constraints)


if __name__ == '__main__':
    australia = create_australia_csp()
    result = australia.backtracking_search()
    for area, color in sorted(result.items()):
        print("{}: {}".format(area, color))

    # Check at https://mapchart.net/australia.html
