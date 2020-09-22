def solution(prices):
    answer = [0 for _ in range(len(prices))]
    if len(prices) >= 2:
        for i in range(1, len(prices)):
            current = prices[i-1]
            count = 0
            for j in range(i, len(prices)):
                comp = prices[j]
                count += 1
                if comp < current:
                    break
            answer[i-1] = count

    return answer

a = [1,2,3,2,3]
print(solution(a))
