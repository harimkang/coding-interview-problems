"""
LeetCode 4. Median of Two Sorted Arrays
url: https://leetcode.com/problems/median-of-two-sorted-arrays/
writer: Harim Kang
Language: Python3
Date: 2021.01.02
Status: Success, Runtime: 84 ms, Memory Usage: 14.5 MB
Follow up: The overall run time complexity should be O(log (m+n)).
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        s = nums1 + nums2
        s.sort()
        if len(s) >= 2:
            if len(s) % 2 == 0:
                ind = len(s) // 2
                return (s[ind - 1] + s[ind]) / 2
            else:
                return float(s[len(s) // 2])
        elif len(s) == 1:
            return float(s[0])
        else:
            return float(0)


if __name__ == "__main__":
    test_cases = [
        [[1, 3], [2]],
        [[1, 2], [3, 4]],
        [[0, 0], [0, 0]],
        [[], [1]],
        [[2], []],
    ]
    expected = [float(2), float(2.5), float(0), float(1), float(2)]
    for i in range(len(test_cases)):
        l1, l2 = test_cases[i]
        expect = expected[i]
        ans = Solution().findMedianSortedArrays(l1, l2)
        if ans == expect:
            print(f"PASSED: {ans} == {expect}")
        else:
            print(f"FAILED: {ans} != {expect}")
