"""Find the Largest Increasing Subsequence.

"""


def find_lis(seq_a: list):
    """Find the largest increasing subsequence. Return itself and it's length.

        Keyword Args:
            seq_a -- first sequence (list)

    """
    lis_reverse = []
    lis = []
    is_matrix = [0] * (len(seq_a) + 1)
    for i in range(1, len(seq_a) + 1):
        cur_max = 0
        for j in range(1, i):
            if seq_a[i - 1] > seq_a[j - 1] and is_matrix[j] > cur_max:
                cur_max = is_matrix[j]
        is_matrix[i] = cur_max + 1
    cur_max = max(is_matrix)
    for i in range(len(seq_a), 0, -1):
        if is_matrix[i] == cur_max and (not len(lis_reverse)
                                        or lis_reverse[-1] > seq_a[i - 1]):
            lis_reverse.append(seq_a[i - 1])
            cur_max -= 1
    for i in range(len(lis_reverse) - 1, -1, -1):
        lis.append(lis_reverse[i])
    return max(is_matrix), lis


def test_find_lis():
    """Common tests for module.

    """
    seq_a = [1, 3, 2]
    lis = [1, 2]
    res = 2
    test_case_lis(seq_a, res, lis, "1")

    seq_a = [6, 10, 4, 7, 2, 11]
    lis = [4, 7, 11]
    res = 3
    test_case_lis(seq_a, res, lis, "2")

    seq_a = [5, 1, 5, 3, 1, 4]
    lis = [1, 3, 4]
    res = 3
    test_case_lis(seq_a, res, lis, "3")

    seq_a = [1, 1]
    lis = [1]
    res = 1
    test_case_lis(seq_a, res, lis, "4")

    seq_a = [7, 20, 4, 11, 23, 5, 33, 3, 1, 6]
    lis = [4, 11, 23, 33]
    res = 4
    test_case_lis(seq_a, res, lis, "5")


def test_case_lis(seq_a, res, lis_res, case_name):
    """Test case for grasshopper's routs.

    """
    print("testcase routs #", case_name, ": ", end="")
    res_counted, lis_counted = find_lis(seq_a)
    print("Ok" if res == res_counted else "Fail", res_counted, sep=": ")
    print("Ok" if lis_res == lis_counted else "Fail", lis_counted, sep=": ")


if __name__ == "__main__":
    test_find_lis()
