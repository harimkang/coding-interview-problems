"""
Baekjoon 2306. 유전자
url: https://www.acmicpc.net/problem/2306
writer: Harim Kang
Language: Python3
Date: 2021.01.09
Status: Success, Runtime: 640 ms, Memory Usage: 34252 KB
"""

dna = input()
len_dna = len(dna)

dp = [[0 for _ in range(len_dna)] for _ in range(len_dna)]

i, j = 0, 1

answer = 0
while i <= j:
    dp[i][j] = dp[i + 1][j - 1]
    if (dna[i] == 'a' and dna[j] == 't') or (dna[i] == 'g' and dna[j] == 'c'):
        dp[i][j] += 2
        if dp[i][j] >= answer:
            answer = dp[i][j]
    j += 1
    