"""Find the Largest Common Subsequence.

"""


def find_lcs(seq_a: list, seq_b: list):
    """Find the largest common subsequence. Return itself and it's length.

        Keyword Args:
            seq_a -- first sequence (list)
            seq_b -- second sequence (list)

    """
    lcs_reverse = []
    lcs = []
    cs_matrix = [[0] * (len(seq_b) + 1) for i in range(len(seq_a) + 1)]
    for i in range(1, len(seq_a) + 1):
        for j in range(1, len(seq_b) + 1):
            if seq_a[i - 1] == seq_b[j - 1]:
                cs_matrix[i][j] = 1 + cs_matrix[i - 1][j - 1]
            else:
                cs_matrix[i][j] = max(cs_matrix[i - 1][j], cs_matrix[i][j - 1])

    i = len(seq_a)
    j = len(seq_b)
    while 1 == 1:
        if cs_matrix[i][j] == cs_matrix[i - 1][j]:
            i -= 1
        elif cs_matrix[i][j] == cs_matrix[i][j - 1]:
            j -= 1
        else:
            lcs_reverse.append(seq_a[i - 1])
            j -= 1
        if cs_matrix[i - 1][j] == 0 and cs_matrix[i][j - 1] == 0:
            lcs_reverse.append(seq_a[i - 1])
            break

    for i in range(len(lcs_reverse) - 1, -1, -1):
        lcs.append(lcs_reverse[i])

    return cs_matrix[-1][-1], lcs


def test_find_lcs():
    """Common tests for module.

    """
    seq_a = [1, 2, 3, 4, 5]
    seq_b = [4, 3, 2, 3, 6, 5]
    lcs = [2, 3, 5]
    res = 3
    test_case_lcs(seq_a, seq_b, res, lcs, "1")

    seq_a = [6, 10, 4, 7, 2, 11]
    seq_b = [10, 4, 8, 5, 6, 7, 1, 4, 3, 2, 11]
    lcs = [10, 4, 7, 2, 11]
    res = 5
    test_case_lcs(seq_a, seq_b, res, lcs, "2")

    seq_a = [5, 1, 5, 3, 1, 4]
    seq_b = [4, 1, 3, 1, 6]
    lcs = [1, 3, 1]
    res = 3
    test_case_lcs(seq_a, seq_b, res, lcs, "3")

    seq_a = [1, 1]
    seq_b = [1, 1, 1, 1, 1]
    lcs = [1, 1]
    res = 2
    test_case_lcs(seq_a, seq_b, res, lcs, "4")

    seq_a = [7, 20, 4, 11, 23, 33, 3, 1, 6]
    seq_b = [10, 3, 4, 4, 6, 3, 23, 1, 4, 10, 21, 6, 4, 5, 1]
    lcs = [4, 23, 1, 6]
    res = 4
    test_case_lcs(seq_a, seq_b, res, lcs, "5")


def test_case_lcs(seq_a, seq_b, res, lcs_res, case_name):
    """Test case for grasshopper's routs.

    """
    print("testcase routs #", case_name, ": ", end="")
    res_counted, lcs_counted = find_lcs(seq_a, seq_b)
    print("Ok" if res == res_counted else "Fail", res_counted, sep=": ")
    print("Ok" if lcs_res == lcs_counted else "Fail", lcs_counted, sep=": ")


if __name__ == "__main__":
    test_find_lcs()
