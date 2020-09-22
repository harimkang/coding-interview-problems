"""
LeetCode 77. Combinations
url: https://leetcode.com/problems/combinations/
writer: Harim Kang
Language: Python3
Date: 2020.09.10
Status: Success, Runtime: 696 ms, Memory Usage: 15.1 MB
(Check) : Don't Use itertools Library
"""


class Solution:
    # If use itertools -> 76ms
    # return list(itertools.combinations(range(1, n+1),k))
    def combine(self, n, k):
        if n < k:
            return []

        answer = []
        num_list = [i + 1 for i in range(n)]
        if n == k:
            return [num_list]

        def dfs(index, path):
            if len(path) == k:
                answer.append(path)
                return

            for i in range(index, len(num_list)):
                if num_list[i] not in path:
                    dfs(i+1, path + [num_list[i]])

        for n in range(len(num_list) - k + 1):
            dfs(n, [num_list[n]])

        return answer


if __name__ == "__main__":
    a, b = 4, 2
    output_1 = [
        [2, 4],
        [3, 4],
        [2, 3],
        [1, 2],
        [1, 3],
        [1, 4],
    ]
    answer_1 = Solution().combine(a, b)
    if sorted(answer_1) == sorted(output_1):
        print('Success: {}'.format(answer_1))
    else:
        print('Failed: {}'.format(answer_1))
