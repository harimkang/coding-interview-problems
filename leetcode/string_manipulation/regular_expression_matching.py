"""
LeetCode 10. Regular Expression Matching
url: https://leetcode.com/problems/regular-expression-matching/
writer: Harim Kang
Language: Python3
Date: 2021.01.07
Status: Success, Runtime: 76 ms, Memory Usage: 14.2 MB
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass


if __name__ == "__main__":
    test_cases = [['aa', 'a'], ['aa', 'a*'], ['ab', '.*'], ['aab', 'c*a*'], ['mississippi', 'mis*is*p*.']]
    expected = [False, True, True, True, False]
    for i in range(len(test_cases)):
        s1 = test_cases[i]
        expect = expected[i]
        ans = Solution().isPalindrome(s1)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
