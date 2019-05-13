"""
https://leetcode.com/problems/subsets/

78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List, Tuple, Any

IntList = List[int]
TupleList = Tuple[Any]


class Solution:
    def subsets(self, nums: IntList) -> TupleList:
        nt = tuple(nums)
        if len(nt) is 0:
            return set()
        elif len(nt) is 1:
            return (), (nums[-1],)
        else:
            # remove a smaller list by removing the last number.
            # get a previous value by computing subsets of the
            # smaller list.
            pv = self.subsets(nums[:-1])

            # to each subset in the previous value add the last number.
            return pv + tuple(s + (nums[-1],) for s in pv)

