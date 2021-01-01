"""
LeetCode 42. Trapping Rain Water
url: https://leetcode.com/problems/trapping-rain-water/
writer: Harim Kang
Language: Python3
Date: 2020.09.08
Status: Success, Runtime: 52 ms, Memory Usage: 14.5 MB
"""


class Solution:
    def trap(self, height):
        # No Exception Case -> Error
        if not height:
            return 0

        left, right = 0, len(height) - 1
        answer = 0
        max_left, max_right = height[left], height[-1]
        while left < right:
            max_left, max_right = max(max_left, height[left]), max(
                max_right, height[right]
            )
            if max_left >= max_right:
                answer += max_right - height[right]
                right -= 1
            else:
                answer += max_left - height[left]
                left += 1

        return answer


if __name__ == "__main__":
    input_1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(Solution().trap(input_1))
    input_2 = []
    print(Solution().trap(input_2))
