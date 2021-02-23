"""Generate grasshopper's routs into selected step and solve two tasks:
   * Grasshopper can move 1, 2 or 3 steps forward. Some steps may be
     not allowed for hop.
   * Grasshopper can move 1 and 2 steps forward. Each step costs it's own price.
     It needs to find the route with minimum total cost.

"""


def count_gh_routs(final_step: int, allowed_steps: list):
    """Calculate amount of grasshopper's routs to get the final_step.

    Keyword arguments:
        final_step -- the destination of grasshopper (int)
        allowed_steps -- allowed steps for grasshopper (list)

    """
    res_list = [1, allowed_steps[1] * 2, allowed_steps[2]
                * (allowed_steps[1] * 2 + 2)] + [0] * (final_step - 3)
    i = int()
    if final_step > 3:
        for i in range(3, final_step):
            if allowed_steps[i]:
                res_list[i] = res_list[i - 1] + res_list[i - 2] + res_list[i - 3]
    else:
        i = final_step - 1
    return res_list[i]


def count_min_cost(final_step: int, prices: list):
    """Calculate min cost of getting to the final step
        and generate this route.

    Keyword arguments:
        final_step -- the destination of grasshopper (int)
        prices -- prices of steps (list)

    """
    min_cost_route = []
    costs_list = [prices[0], prices[1]] + [0] * (final_step - 2)
    i = int()
    for i in range(2, final_step):
        costs_list[i] = prices[i] + min(costs_list[i - 1], costs_list[i - 2])
        if costs_list[i - 1] < costs_list[i - 2] \
                and (not len(min_cost_route) or i - 1 != min_cost_route[-1]):
            min_cost_route.append(i - 1)
        elif not len(min_cost_route) or i - 2 != min_cost_route[-1]:
            min_cost_route.append(i - 2)
    min_cost_route.append(i)

    return costs_list[i], min_cost_route


def test_gh():
    """Common tests for module.

    """
    final_step = 3
    res = 4
    test_case_gh(final_step, res, None, "1")

    final_step = 4
    res = 7
    test_case_gh(final_step, res, None, "2")

    final_step = 5
    res = 13
    test_case_gh(final_step, res, None, "3")

    final_step = 6
    res = 24
    test_case_gh(final_step, res, None, "4")

    final_step = 3
    res = 2
    test_case_gh(final_step, res, [1, 0, 1], "5")

    final_step = 4
    res = 0
    test_case_gh(final_step, res, [1, 0, 1, 0], "6")

    final_step = 4
    res = 3
    test_case_gh(final_step, res, [1, 0, 1, 1], "7")

    final_step = 4
    res = 3
    test_case_gh(final_step, res, [1, 1, 0, 1], "8")

    final_step = 5
    res = 5
    test_case_gh(final_step, res, [1, 1, 0, 1, 1], "9")

    final_step = 5
    res = 6
    test_case_gh(final_step, res, [1, 1, 1, 0, 1], "10")

    final_step = 3
    res_min_cost = 4
    res_min_route = [1, 2]
    test_case_gh_cost(final_step, res_min_cost, res_min_route, [5, 3, 1], "1")

    final_step = 4
    res_min_cost = 5
    res_min_route = [0, 2, 3]
    test_case_gh_cost(final_step, res_min_cost, res_min_route, [2, 6, 1, 2], "2")

    final_step = 5
    res_min_cost = 6
    res_min_route = [1, 3, 4]
    test_case_gh_cost(final_step, res_min_cost, res_min_route, [15, 4, 11, 0, 2], "3")


def test_case_gh(final_step, res, allowed_steps, case_name):
    """Test case for grasshopper's routs.

    """
    print("testcase routs #", case_name, ": ", end="")
    allowed_steps = [1] * final_step if allowed_steps is None else \
        allowed_steps
    res_counted = count_gh_routs(final_step, allowed_steps)
    print("Ok" if res == res_counted else "Fail", res_counted, sep=": ")


def test_case_gh_cost(final_step, res_min_cost, res_min_route, prices, case_name):
    """Test case for grasshopper's routs minimal costs.

    """
    print("testcase costs #", case_name, ": ", end="")
    res_min_cost_counted, res_min_route_counted = count_min_cost(final_step, prices)
    print("min cost is ok" if res_min_cost == res_min_cost_counted else "Fail",
          res_min_cost_counted, sep=": ")
    print("min route is ok" if res_min_route == res_min_route_counted else "Fail",
          res_min_route_counted, sep=": ")


if __name__ == "__main__":
    test_gh()
