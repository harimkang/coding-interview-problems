import heapq


def solution(operations):

    # pq 는 최소힙, max_pq 는 최대힙(-가 붙어서 반대로 정렬)
    pq = []
    max_pq = []

    # 삽입 명령 수행 함수
    def insert(num):
        # 숫자를 pq 에 힙정렬로 넣고(오름차순), max_pq 에는 -를 붙여서 넣는다(내림차순)
        heapq.heappush(pq, num)
        heapq.heappush(max_pq, -num)

    # 삭제 명령 수행 함수
    def delete(a, b):
        # a 가 max_pq 이고, b가 pq 이면 최대값 삭제
        # 반대의 경우엔 최소값 삭제
        if a and b:
            target = -heapq.heappop(a)
            temp = []
            while b:
                c = heapq.heappop(b)
                if target == c:
                    break
                else:
                    temp.append(c)
            if temp:
                for d in temp:
                    heapq.heappush(b, d)

    # 명령을 수행하는 구절
    for op in operations:
        op = op.split()
        op[1] = int(op[1])
        if op[0] == "D":
            if op[1] == 1:
                delete(max_pq, pq)
            elif op[1] == -1:
                delete(pq, max_pq)
        elif op[0] == "I":
            insert(op[1])

    if pq:
        min_num = heapq.heappop(pq)
        max_num = -heapq.heappop(max_pq)
    else:
        min_num, max_num = 0, 0
    answer = [max_num, min_num]
    return answer


o = ["I 16", "D 1"]
o2 = ["I 7", "I 5", "I -5", "D -1"]

print(solution(o))
print(solution(o2))
