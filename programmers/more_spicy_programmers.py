import heapq


def solution(scoville, K):
    answer = 0
    heap = []
    for h in scoville:
        heapq.heappush(heap, h)
    while True:
        current = heapq.heappop(heap)
        if len(heap) < 1 and current < K:
            answer = -1
            break
        if current >= K:
            break
        else:
            answer += 1
            next_node = heapq.heappop(heap)
            heapq.heappush(heap, current + next_node * 2)

    return answer


sc = [1, 2, 3, 9, 10, 12]
k = 7
print(solution(sc, k))
