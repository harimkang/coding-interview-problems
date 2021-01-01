def solution(N):
    if N == 1:
        return 4
    elif N >= 2:
        tile = [0 for _ in range(N + 1)]
        dp = [0 for _ in range(N + 1)]
        tile[1] = 1
        dp[1] = 4
        for i in range(2, N + 1):
            tile[i] = tile[i - 2] + tile[i - 1]
            dp[i] = dp[i - 1] + 2 * tile[i]
        answer = dp[N]
        return answer
