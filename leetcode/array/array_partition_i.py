"""
LeetCode 561. Array Partition I
url: https://leetcode.com/problems/array-partition-i/
writer: Harim Kang
Language: Python3
Date: 2020.09.09
Status: Success, Runtime: 272 ms, Memory Usage: 16.2 MB
"""


class Solution:
    def arrayPairSum(self, nums):

        nums.sort()

        return sum(nums[::2])


if __name__ == "__main__":
    input_1 = [1, 4, 3, 2]
    print(Solution().arrayPairSum(input_1))
