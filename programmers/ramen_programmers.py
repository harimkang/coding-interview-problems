import heapq


def solution(stock, dates, supplies, k):
    answer = 0

    pq = []
    i = 0
    while stock < k:
        # 목표 : 재고가 k 이상이면 밀가루가 충분
        # 현재 재고가 k보다 작을 때
        while i < len(dates) and dates[i] <= stock:
            # 해당 반복문에는 반드시 1번은 들어온다. (제한 조건에 의해)
            # 날짜를 증가 시키면서 공급일보다 stock 이 커질 때
            # 즉, 공급일에 도달하면 해당 공급량을 heap 에 push 한다.
            heapq.heappush(pq, -supplies[i])
            i += 1
        # 현재 공급일까지의 공급량 중 가장 큰 수를 추가
        # 해당 공급량이 부족하면 반복
        stock += -heapq.heappop(pq)
        answer += 1

    return answer


st = 4
da = [4, 10, 15]
sup = [20, 5, 10]
_k = 30
print(solution(st, da, sup, _k))
