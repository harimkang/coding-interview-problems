import heapq


def solution(routes):
    answer = 0
    point = []
    ck = [0 for _ in routes]
    for a, b in routes:
        point.append(a)
        point.append(b)
    point = list(set(point))
    point.sort()

    heap = []
    for p in point:
        temp = [0 for _ in routes]
        for i in range(len(routes)):
            if routes[i][0] <= p <= routes[i][1]:
                temp[i] = 1
        heapq.heappush(heap, [-sum(temp), -p, temp])
    past = []
    while 0 in ck:
        _, po, r = heapq.heappop(heap)
        if r in past:
            continue
        past.append(r)
        for i in range(len(ck)):
            if r[i] == 1:
                ck[i] += 1

        answer += 1

    return answer


tc = [[[-20, 15], [-14, -5], [-18, -13], [-5, -3]]]
for c in tc:
    print(solution(c))
