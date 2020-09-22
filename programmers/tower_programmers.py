def solution(heights):

    answer = [0 for _ in range(len(heights))]
    for i in reversed(range(len(heights))):
        cur = 0
        for j in range(i):
            if heights[i] < heights[j]:
                cur = j + 1
        answer[i] = cur
    return answer
