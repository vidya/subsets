from subsets.subsets import Solution


def test_1_basic():
    nums = [1]
    expected = ((), (1,))

    result = Solution().subsets(nums)
    assert set(result) == set(expected)


def test_2_basic():
    nums = [1, 2]
    expected = ((), (1,), (2,), (1, 2))

    result = Solution().subsets(nums)
    assert set(result) == set(expected)


def test_3_basic():
    nums = [1, 2, 3]
    expected = ((),
                (1,), (2,), (3,),
                (1, 2), (1, 3), (2, 3),
                (1, 2, 3)
                )

    result = Solution().subsets(nums)
    assert set(result) == set(expected)

