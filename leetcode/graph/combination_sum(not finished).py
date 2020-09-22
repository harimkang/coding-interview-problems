"""
LeetCode 39. Combination Sum
url: https://leetcode.com/problems/combination-sum/
writer: Harim Kang
Language: Python3
Date: 2020.09.10
Status: Success, Runtime: 696 ms, Memory Usage: 15.1 MB
(Check) : Don't Use itertools Library
"""


class Solution:
    def combinationSum(self, candidates, target):
        return []


if __name__ == "__main__":
    a, b = [2, 3, 6, 7], 7
    output_1 = [
        [7],
        [2, 2, 3]
    ]
    answer_1 = Solution().combinationSum(a, b)
    if sorted(answer_1) == sorted(output_1):
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))

    a, b = [2, 3, 5], 8
    output_1 = [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
    answer_1 = Solution().combinationSum(a, b)
    if sorted(answer_1) == sorted(output_1):
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))
