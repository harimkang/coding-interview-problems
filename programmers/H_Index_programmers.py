def solution(citations):
    answer = 0
    for h in range(max(citations) + 1):
        x = [1 for _ in citations if _ >= h]
        if answer <= h <= len(x):
            answer = h

    return answer


tc = [[3, 0, 6, 1, 5], [0, 6, 6, 4, 5], [5, 5, 5, 0], [8, 8, 8, 0]]
for c in tc:
    print(solution(c))