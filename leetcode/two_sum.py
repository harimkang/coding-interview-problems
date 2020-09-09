"""
LeetCode 1. Two Sum
url: https://leetcode.com/problems/two-sum/
writer: Harim Kang
Language: Python3
Date: 2020.09.07
Status: Success, Runtime: 44 ms, Memory Usage: 15.3 MB
"""


class Solution:
    def twoSum(self, nums, target):
        # Method 1
        # Status: Success, Runtime: 1092 ms, Memory Usage: 14.9 MB
        # for i in range(len(nums)-1):
        #     if target - nums[i] in nums[i+1:]:
        #         index = nums[i+1:].index(target - nums[i])
        #         return [i, index + i + 1]

        # Method 2
        # Status: Success, Runtime: 44 ms, Memory Usage: 15.3 MB
        temp_map = {}
        for i in range(len(nums)):
            _t = target - nums[i]
            if _t in temp_map:
                return [temp_map[_t], i]
            else:
                temp_map[nums[i]] = i


if __name__ == "__main__":
    input_1, target_1 = [2, 7, 11, 15], 9
    print(Solution().twoSum(input_1, target_1))
    input_2, target_2 = [3, 2, 4], 6
    print(Solution().twoSum(input_2, target_2))
    input_3, target_3 = [3, 3], 6
    print(Solution().twoSum(input_3, target_3))
