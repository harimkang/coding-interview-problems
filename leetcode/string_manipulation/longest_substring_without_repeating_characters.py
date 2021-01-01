"""
LeetCode 3. Longest Substring Without Repeating Characters
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
writer: Harim Kang
Language: Python3
Date: 2021. 01. 01
Status: Success, Runtime: 76 ms, Memory Usage: 14.8 MB
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        len_list = [0 for _ in s]
        len_list[0] = 1
        temp = [s[0]]
        for i in range(1, len(s)):
            if s[i] in temp:
                index_same = temp.index(s[i])
                temp = temp[index_same + 1 :]
                temp.append(s[i])
                len_list[i] = len(temp)
            else:
                len_list[i] = len_list[i - 1] + 1
                temp.append(s[i])

        return max(len_list)


if __name__ == "__main__":
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", ""]
    expected = [3, 1, 3, 0]

    for i in range(len(test_cases)):
        sol = Solution()
        ans = sol.lengthOfLongestSubstring(test_cases[i])
        print(ans)
        if ans == expected[i]:
            print(f"PASSED: {i}")
