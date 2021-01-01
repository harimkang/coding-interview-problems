"""
LeetCode 5. Longest Palindromic Substring
url: https://leetcode.com/problems/longest-palindromic-substring/
writer: Harim Kang
Language: Python3
Date: 2020.09.03
Status: Success, Runtime: 5424 ms, Memory Usage: 14 MB
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(_s):
            if _s == _s[::-1]:
                return True
            return False

        answer = ""
        if len(s) <= 1 or is_palindrome(s):
            return s

        for i in range(len(s) - 1):
            if len(s[i]) > len(answer):
                answer = s[i]
            for j in range(i + 1, len(s)):
                if is_palindrome(s[i : j + 1]) and len(s[i : j + 1]) > len(answer):
                    answer = s[i : j + 1]

        return answer


if __name__ == "__main__":
    input_1 = "babad"
    print(Solution().longestPalindrome(input_1))
    input_2 = "cbbd"
    print(Solution().longestPalindrome(input_2))
    input_3 = "bb"
    print(Solution().longestPalindrome(input_3))
