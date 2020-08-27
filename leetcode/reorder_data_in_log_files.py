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
            # isdigit -> Check Digit, if Digit, then True
            if log[1].isdigit():
                digit_logs.append(" ".join(log))
            else:
                letter_logs.append(" ".join(log))

        # 2nd [1] element key sorting
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter_logs + digit_logs


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(Solution().reorderLogFiles(logs))
