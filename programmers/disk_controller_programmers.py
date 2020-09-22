import heapq


def solution(jobs):
    n = len(jobs)
    # jobs 를 p_queue 로 변경 --> jobs 가 들어오는 순서대로 정렬된다.
    heapq.heapify(jobs)
    # 맨 처음꺼 꺼내보겠음 --> 젤 처음 시작하는게 나오겠지>?
    current, length = heapq.heappop(jobs)
    answer = 0
    pq = []
    # pq 라는 큐를 하나 더 사용해보겠음, 이건 현재 값에서 작업 길이를 추가한 걸로 정렬
    # 즉, 예측했을 때 결과 값을 오름차순
    # 맨처음 꺼를 pq에 넣어보겠음
    heapq.heappush(pq, (current + length, current, length))
    while pq:
        # pq에 있는 첫번째꺼(계산 값이 젤 작은 거)를 꺼냅니다.
        # current 는 선택한 작업이 끝난 시점
        current, start, length = heapq.heappop(pq)
        # answer 계산
        answer = answer - start + current
        while pq:
            # 여기 반복문은 pq를 비우고 jobs 에 채웁니다.
            _, c, d = heapq.heappop(pq)
            heapq.heappush(jobs, [c, d])
        while jobs:
            # jobs 에 남은 작업 중에 시작점이 current 보다
            # 작은 것들을 빼서 pq에 계산해서 넣어보겠슴
            if jobs[0][0] > current:
                # jobs 중 젤 작은게 current 보다 작아지면 반복문을 벗어나
                if not pq:
                    # 만약에 pq가 비었는데 jobs 는 존재할때,
                    # 즉, 도착한 작업이 없고 대기 작업은 존재할때
                    e, f = heapq.heappop(jobs)
                    heapq.heappush(pq, (e+f, e, f))
                break
            else:
                # current 보다 시작점이 작으면 가능한 경우이기 때문에 pq에 넣어봄
                a, b = heapq.heappop(jobs)
                heapq.heappush(pq, (current + b, a, b))

    answer /= n
    # 마무리

    return int(answer)


jo = [[0, 3], [1, 9], [2, 6]]
jo2 = [[0, 1], [1, 2], [2, 5], [3, 3]]
jo3 = [[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]]
jo4 = [[0, 3], [4, 4], [5, 3], [4, 1]]
print(solution(jo))
print(solution(jo2))
print(solution(jo3))
print(solution(jo4))