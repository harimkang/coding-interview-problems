"""
LeetCode 8. String to Integer (atoi)
url: https://leetcode.com/problems/string-to-integer-atoi/
writer: Harim Kang
Language: Python3
Date: 2021.01.05
Status: Success, Runtime: 28 ms, Memory Usage: 14.2 MB
"""

import re


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        i = 0
        if s:
            if s[0].isdigit():
                i = int(re.findall("\d+", s)[0])
            elif s[0] in ["-", "+"] and len(s) >= 2 and s[1].isdigit():
                i = int(re.findall("\d+", s)[0])
                if s[0] == "-":
                    i = -i

        if i < -(2 ** 31):
            i = -(2 ** 31)
        elif i > 2 ** 31 - 1:
            i = 2 ** 31 - 1

        return i


if __name__ == "__main__":
    test_cases = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "+-12",
        "+1",
    ]
    expected = [42, -42, 4193, 0, -2147483648, 0, 1]
    for i in range(len(test_cases)):
        s1 = test_cases[i]
        expect = expected[i]
        ans = Solution().myAtoi(s1)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
