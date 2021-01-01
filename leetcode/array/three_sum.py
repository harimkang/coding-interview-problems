"""
LeetCode 15. 3 Sum
url: https://leetcode.com/problems/3sum/
writer: Harim Kang
Language: Python3
Date: 2020.09.09
Status: Success, Runtime: 924 ms, Memory Usage: 17.4 MB
"""


class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        answer = []

        # Array Sort O(nlogn)
        nums.sort()

        # Maximum O(n**2)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Using Two Point Method
            left, right = i + 1, len(nums) - 1
            while left < right:
                h_sum = nums[i] + nums[left] + nums[right]
                if h_sum < 0:
                    left += 1
                elif h_sum > 0:
                    right -= 1
                else:
                    # if sum == 0
                    # Append to answer
                    answer.append([nums[i], nums[left], nums[right]])

                    # Skip Duplication Case
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return answer


if __name__ == "__main__":
    input_1 = [-1, 0, 1, 2, -1, -4]
    print(Solution().threeSum(input_1))
    input_2 = []
    print(Solution().threeSum(input_2))
    input_3 = [0]
    print(Solution().threeSum(input_3))
