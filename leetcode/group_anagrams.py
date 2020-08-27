"""
LeetCode 49. Group Anagrams
url: https://leetcode.com/problems/group-anagrams/
writer: Harim Kang
Language: Python3
Date: 2020.08.28
Status: Success, Runtime: 92 ms, Memory Usage: 16.5 MB
"""


class Solution:
    def groupAnagrams(self, strs):

        dic = {}
        group = []
        for a in strs:
            b = ''.join(sorted(a))
            if b in dic:
                dic[b].append(a)
            else:
                dic[b] = [a]

        for value in dic.values():
            group.append(value)

        return group


if __name__ == "__main__":
    input_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(input_1))
