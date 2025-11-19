from pulp import LpMaximize, LpProblem, LpStatus, LpVariable, PULP_CBC_CMD, value  # type: ignore

def optimize_chocolates():
    # Define the optimization problem
    model = LpProblem("Chocolate_Production", LpMaximize)

    # Decision variables (non-negative)
    units_a = LpVariable("Units_A", lowBound=0)
    units_b = LpVariable("Units_B", lowBound=0)

    # Objective: Maximize profit = 6*A + 5*B
    model += 6 * units_a + 5 * units_b

    # Constraints
    model += units_a + units_b <= 5, "Milk"
    model += 3 * units_a + 2 * units_b <= 12, "Choco"

    # Solve the model
    status = model.solve(PULP_CBC_CMD(msg=False))

    return {
        "status": LpStatus[status],
        "units_a": value(units_a),
        "units_b": value(units_b),
        "max_profit": value(model.objective),
    }

if __name__ == "__main__":
    solution = optimize_chocolates()
    print(f"Status: {solution['status']}")
    print(f"Produce {solution['units_a']} units of A")
    print(f"Produce {solution['units_b']} units of B")
    print(f"Maximum Profit: Rs {solution['max_profit']}")
