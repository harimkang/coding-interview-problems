def solution(n, costs):
    answer = 0
    island = []
    node = []
    costs.sort(key=lambda a: a[2])

    while True:
        pass

    return answer


tc = [
    [4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]],
    [5, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 3], [2, 3, 8], [3, 4, 1]]],
]
for n_1, c1 in tc:
    print(solution(n_1, c1))
