"""
LeetCode 9. Palindrome Number
url: https://leetcode.com/problems/palindrome-number/
writer: Harim Kang
Language: Python3
Date: 2021.01.06
Status: Success, Runtime: 76 ms, Memory Usage: 14.2 MB
Follow up: Could you solve it without converting the integer to a string?
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        answer = []
        while x >= 10:
            r = x % 10
            x = x // 10
            answer.append(r)
        answer.append(x)

        return answer == answer[::-1]


if __name__ == "__main__":
    test_cases = [121, -121, 10, -101]
    expected = [True, False, False, False]
    for i in range(len(test_cases)):
        s1 = test_cases[i]
        expect = expected[i]
        ans = Solution().isPalindrome(s1)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
