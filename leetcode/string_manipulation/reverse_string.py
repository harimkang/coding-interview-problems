"""
LeetCode 344. Reverse String
url: https://leetcode.com/problems/reverse-string/
writer: Harim Kang
Language: Python3
Date: 2020.08.24
Status: Success, Runtime: 216 ms, Memory Usage: 18.4 MB
"""


class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]


if __name__ == "__main__":
    input_1 = ["h", "e", "l", "l", "o"]
    Solution().reverseString(input_1)
    input_2 = ["H", "a", "n", "n", "a", "h"]
    Solution().reverseString(input_2)
