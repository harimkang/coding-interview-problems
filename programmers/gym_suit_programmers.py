def solution(n, lost, reserve):
    num = len(lost)
    for i in range(num):
        if lost[i] in reserve:
            num -= 1
            reserve.remove(lost[i])
            lost[i] = 0
    for id_num in lost:
        if id_num == 0:
            continue
        if id_num in reserve:
            num -= 1
            reserve.remove(id_num)
            continue
        if id_num - 1 in reserve:
            num -= 1
            reserve.remove(id_num - 1)
            continue
        if id_num + 1 in reserve:
            num -= 1
            reserve.remove(id_num + 1)
    answer = n - num
    return answer


tc = [[5, [2, 4], [1, 3, 5]], [5, [2, 4], [3]], [3, [3], [1]],
      [10, [3, 9, 10], [3, 8, 9]]]
for a, l, r in tc:
    print(solution(a, l, r))