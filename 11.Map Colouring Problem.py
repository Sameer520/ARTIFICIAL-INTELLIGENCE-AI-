class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.assignment = {}

    def is_consistent(self, variable, value):
        for neighbor in self.constraints.get(variable, []):
            if neighbor in self.assignment and self.assignment[neighbor] == value:
                return False
        return True

    def backtrack(self):
        if len(self.assignment) == len(self.variables):
            return self.assignment

        unassigned = [v for v in self.variables if v not in self.assignment]
        variable = unassigned[0]

        for value in self.domains[variable]:
            if self.is_consistent(variable, value):
                self.assignment[variable] = value
                result = self.backtrack()
                if result is not None:
                    return result
                del self.assignment[variable]

        return None

def solve_map_coloring():
    num_variables = int(input("Enter the number of regions: "))
    variables = []
    for i in range(num_variables):
        variables.append(input(f"Enter the name of region {i+1}: "))

    domains = {}
    for var in variables:
        colors = input(f"Enter colors for {var} (separate with spaces): ").split()
        domains[var] = colors

    constraints = {}
    for var in variables:
        adjacent = input(f"Enter adjacent regions for {var} (separate with spaces): ").split()
        constraints[var] = adjacent

    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.backtrack()

    if solution:
        print("Solution found:")
        for region, color in solution.items():
            print(f"{region}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    solve_map_coloring()
