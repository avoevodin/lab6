"""Generate grasshopper's routs into selected step and solve two tasks:
   * Grasshopper can move 1, 2 or 3 steps forward. Some steps may be
     not allowed for hop.
   * Grasshopper can move 1 and 2 steps forward. Each step costs it's own price.
     It needs to find the route with minimum total cost.

"""
import unittest

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


if __name__ == '__main__':  # pragma: no cover
    unittest.main(verbosity=2, module='test_grasshopper')
