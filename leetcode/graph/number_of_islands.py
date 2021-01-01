"""
LeetCode 200. Number of Islands
url: https://leetcode.com/problems/number-of-islands/
writer: Harim Kang
Language: Python3
Date: 2020.09.10
Status: Success, Runtime: 164 ms, Memory Usage: 14.8 MB
"""


class Solution:
    grid = None

    def dfs(self, i, j):
        if (
            i < 0
            or i >= len(self.grid)
            or j < 0
            or j >= len(self.grid[0])
            or self.grid[i][j] != "1"
        ):
            return

        self.grid[i][j] = "#"

        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)

    def numIslands(self, grid):
        self.grid = grid
        if not self.grid:
            return 0
        answer = 0
        h, w = len(self.grid), len(self.grid[0])
        for i in range(h):
            for j in range(w):
                if self.grid[i][j] == "1":
                    self.dfs(i, j)
                    answer += 1
        return answer


if __name__ == "__main__":
    input_1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    answer_1 = Solution().numIslands(input_1)
    if answer_1 == 1:
        print("Success: {} == 1".format(answer_1))
    else:
        print("Failed: {} != 1".format(answer_1))
    input_2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    answer_2 = Solution().numIslands(input_2)

    if answer_2 == 3:
        print("Success: {} == 3".format(answer_2))
    else:
        print("Failed: {} != 3".format(answer_2))
