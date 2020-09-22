"""
LeetCode 46. Permutations
url: https://leetcode.com/problems/permutations/
writer: Harim Kang
Language: Python3
Date: 2020.09.10
Status: Success, Runtime: 44 ms, Memory Usage: 13.9 MB
(Check) : Don't Use itertools Library
"""


class Solution:
    # If use itertools -> 36ms
    # return list(itertools.permutations(nums))
    def permute(self, nums):
        answer = []

        def dfs(path):
            if len(path) == len(nums):
                answer.append(path)
                return
            for i in range(len(nums)):
                if nums[i] not in path:
                    temp = path + [nums[i]]
                    dfs(temp)
        for n in nums:
            dfs([n])

        return answer


if __name__ == "__main__":
    input_1 = [1, 2, 3]
    output_1 = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]
    answer_1 = Solution().permute(input_1)
    if answer_1 == output_1:
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))
