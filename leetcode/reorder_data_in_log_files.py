"""
LeetCode 937. Reorder Data in Log Files
url: https://leetcode.com/problems/reorder-data-in-log-files/
writer: Harim Kang
Language: Python3
Date: 2020.08.24
Status: Success, Runtime: 36 ms, Memory Usage: 13.8 MB
"""


class Solution:
    def reorderLogFiles(self, logs):
        letter_logs = []
        digit_logs = []

        for log in logs:
            log = log.split(" ")
            if log[1].isdigit():
                digit_logs.append(" ".join(log))
            else:
                letter_logs.append(" ".join(log))

        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs
