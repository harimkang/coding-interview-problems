import collections
import heapq


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)
    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(start, _ck):
        distance = {_v: float('inf') for _v in graph}
        distance[start] = 0
        q = []
        heapq.heappush(q, [distance[start], start])
        while q:
            try:
                price, node = heapq.heappop(q)
                if distance[node] < price:
                    continue
                for _v, _w in graph[node]:
                    temp = price + _w
                    if temp < distance[_v]:
                        distance[_v] = temp
                        heapq.heappush(q, (temp, _v))
            except RuntimeError:
                continue
        for j in range(len(_ck[start - 1])):
            _ck[start - 1][j] = True
            _ck[j][start - 1] = True

        return distance, _ck

    total = {}
    ck = [[False for _ in range(n)] for _ in range(n)]
    for i in range(1, n + 1):
        total[i], ck = dijkstra(i, ck)
        for j in ck:
            if False in j:
                continue
    answer = []
    for i in range(1, n + 1):
        if i not in [s, a, b]:
            answer.append(total[s][i] + total[i][a] + total[i][b])
    answer.append(total[s][a] + total[a][b])
    answer.append(total[s][b] + total[b][a])
    answer.append(total[s][a] + total[s][b])

    return min(answer)


if __name__ == "__main__":
    test_case = [[6, 4, 6, 2,
                  [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                   [1, 6, 25]]],
                 [7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]],
                 [6, 4, 5, 6,
                  [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]]
                 ]

    for N, S, A, B, fa in test_case:
        print(solution(N, S, A, B, fa))
