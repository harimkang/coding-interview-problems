"""
LeetCode 7. Reverse Integer
url: https://leetcode.com/problems/reverse-integer/
writer: Harim Kang
Language: Python3
Date: 2021.01.04
Status: Success, Runtime: 32 ms, Memory Usage: 14.1 MB
"""


class Solution:
    def reverse(self, x: int) -> int:
        sub = False
        if x < 0:
            sub = True
            x = -x

        s = str(x)
        s_list = list(s)
        s_list.reverse()
        answer = int("".join(s_list))
        if answer < -(2 ** 31) or answer > (2 ** 31) - 1:
            return 0

        if sub:
            answer = -answer

        return answer


if __name__ == "__main__":
    test_cases = [123, -123, 120, 0, 1534236469]
    expected = [321, -321, 21, 0, 0]
    for i in range(len(test_cases)):
        s1 = test_cases[i]
        expect = expected[i]
        ans = Solution().reverse(s1)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
