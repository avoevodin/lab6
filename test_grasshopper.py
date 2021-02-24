import unittest
from dp_grasshopper import count_min_cost, count_gh_routs


class GrasshopperRoutesTestCase(unittest.TestCase):
    def test_case_gh_1(self):
        final_step = 3
        res = 4
        allowed_steps = [1] * final_step
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_2(self):
        final_step = 4
        res = 7
        allowed_steps = [1] * final_step
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_3(self):
        final_step = 5
        res = 13
        allowed_steps = [1] * final_step
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_4(self):
        final_step = 6
        res = 24
        allowed_steps = [1] * final_step
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_5(self):
        final_step = 3
        res = 2
        allowed_steps = [1, 0, 1]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_6(self):
        final_step = 4
        res = 0
        allowed_steps = [1, 0, 1, 0]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_7(self):
        final_step = 4
        res = 3
        allowed_steps = [1, 0, 1, 1]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_8(self):
        final_step = 4
        res = 3
        allowed_steps = [1, 1, 0, 1]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_9(self):
        final_step = 5
        res = 5
        allowed_steps = [1, 1, 0, 1, 1]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)

    def test_case_gh_10(self):
        final_step = 5
        res = 6
        allowed_steps = [1, 1, 1, 0, 1]
        res_counted = count_gh_routs(final_step, allowed_steps)
        self.assertEqual(res, res_counted)


class GrosshopperMinCostTestCase(unittest.TestCase):
    def test_case_min_cost_1(self):
        final_step = 3
        res_min_cost = 4
        res_min_route = [1, 2]
        prices = [5, 3, 1]
        counted_min_cost, counted_min_route = count_min_cost(final_step, prices)
        self.assertEqual(res_min_cost, counted_min_cost, msg='min cost is wrong')
        self.assertEqual(res_min_route, counted_min_route, msg='min route is wrong')

    def test_case_min_cost_2(self):
        final_step = 4
        res_min_cost = 5
        res_min_route = [0, 2, 3]
        prices = [2, 6, 1, 2]
        counted_min_cost, counted_min_route = count_min_cost(final_step, prices)
        self.assertEqual(res_min_cost, counted_min_cost, msg='min cost is wrong')
        self.assertEqual(res_min_route, counted_min_route, msg='min route is wrong')

    def test_case_min_cost_3(self):
        final_step = 5
        res_min_cost = 6
        res_min_route = [1, 3, 4]
        prices = [15, 4, 11, 0, 2]
        counted_min_cost, counted_min_route = count_min_cost(final_step, prices)
        self.assertEqual(res_min_cost, counted_min_cost, msg='min cost is wrong')
        self.assertEqual(res_min_route, counted_min_route, msg='min route is wrong')
