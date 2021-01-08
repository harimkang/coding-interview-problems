"""
Baekjoon 1260. DFS와 BFS
url: https://www.acmicpc.net/problem/1260
writer: Harim Kang
Language: Python3
Date: 2021.01.08
Status: Success, Runtime: 640 ms, Memory Usage: 34252 MB
"""

from typing import DefaultDict


N, M, V = map(int, input().split())


graph = DefaultDict(list)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.keys():
    graph[i].sort()


def search(s, method):
    # s는 시작 노드를 의미한다. 스택을 사용하여 구현
    visited = [0] * N
    temp = [s]
    path = []

    while temp:
        if method == "dfs":
            current = temp.pop()
            temp_graph = graph[current][::-1]
        else:
            current = temp.pop(0)
            temp_graph = graph[current]

        if visited[current - 1] == 0:
            visited[current - 1] = 1
            path.append(current)
        for node in temp_graph:
            if visited[node - 1] == 0:
                temp.append(node)

    for i in path:
        print(i, end=" ")
    print()


search(V, method="dfs")
search(V, method="bfs")
