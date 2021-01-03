"""
LeetCode 6. ZigZag Conversion
url: https://leetcode.com/problems/zigzag-conversion/
writer: Harim Kang
Language: Python3
Date: 2021.01.03
Status: Success, Runtime: 64 ms, Memory Usage: 14.5 MB
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        temp = [[] for _ in range(numRows)]

        count = 0
        dec = False
        for i in range(len(s)):
            temp[count].append(s[i])

            if count == numRows - 1:
                dec = True
            elif count == 0:
                dec = False

            if dec:
                count -= 1
            else:
                count += 1

        answer = ""
        for t in temp:
            temp_str = "".join(t)
            answer += temp_str

        return answer


if __name__ == "__main__":
    test_cases = [["PAYPALISHIRING", 3], ["PAYPALISHIRING", 4], ["A", 1], ["ABC", 1]]
    expected = ["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A", "ABC"]
    for i in range(len(test_cases)):
        s1, numrows = test_cases[i]
        expect = expected[i]
        ans = Solution().convert(s1, numrows)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
