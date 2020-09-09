"""
LeetCode 238. Product of Array Except Self
url: https://leetcode.com/problems/product-of-array-except-self/
writer: Harim Kang
Language: Python3
Date: 2020.09.09
Status: Success, Runtime: 124 ms, Memory Usage: 20.4 MB
"""


class Solution:
    def productExceptSelf(self, nums):

        # max_product: Product of all numbers except 0
        # num_zero: Number of Zeros
        max_product = 1
        num_zero = 0

        # max_product calculation
        for p in nums:
            if p == 0:
                num_zero += 1
            else:
                max_product *= p

        # Classified according to the number of num_zeros
        if num_zero > 1:
            # 0 for all cases of 2 or more 0s
            return [0 for _ in nums]
        elif num_zero == 1:
            # If there is one 0, only the position with 0 is max_product, the rest are 0
            answer = [0 if nums[i] != 0 else max_product for i in range(len(nums))]
        else:
            # If there is no zero, divide the number at that position by the maximum product normally
            answer = [int(max_product/nums[i]) for i in range(len(nums))]

        return answer


if __name__ == "__main__":
    input_1 = [1, 2, 3, 4]
    print(Solution().productExceptSelf(input_1))
    input_2 = [0, 0]
    print(Solution().productExceptSelf(input_2))
    input_3 = [1, 0]
    print(Solution().productExceptSelf(input_3))
