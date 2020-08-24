"""
LeetCode 125. Valid Palindrome
url: https://leetcode.com/problems/valid-palindrome/
writer: Harim Kang
Language: Python3
Date: 2020.08.24
Status: Success, Runtime: 40 ms, Memory Usage: 19.8 MB
"""
# import re


class Solution:
    # Palindrome Check Function
    def isPalindrome(self, s: str) -> bool:
        # Erase special characters, numbers, and spaces
        pal = []
        for char in s:
            # isalnum -> Check Alphabet, if Alphabet, then True
            if char.isalnum():
                pal.append(char.lower())
        # pal = re.sub('[^a-z0-9]', '', s.lower()) -> Runtime: 32ms, Faster than isalnum

        if pal == pal[::-1]:
            return True
        return False
