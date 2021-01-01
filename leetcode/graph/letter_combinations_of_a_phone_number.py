"""
LeetCode 17. Letter Combinations of a Phone Number
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
writer: Harim Kang
Language: Python3
Date: 2020.09.10
Status: Success, Runtime: 32 ms, Memory Usage: 13.7 MB
"""


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        str_digit = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }

        answer = []

        def dfs(index, path):
            if len(path) == len(digits):
                answer.append(path)
                return
            for i in range(index, len(digits)):
                for j in str_digit[digits[i]]:
                    dfs(i + 1, path + j)

        dfs(0, "")

        return answer


if __name__ == "__main__":
    input_1 = "23"
    answer_1 = Solution().letterCombinations(input_1)
    if answer_1 == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]:
        print("Success: {}".format(answer_1))
    else:
        print("Failed: {}".format(answer_1))
