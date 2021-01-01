def solution(priorities, location):

    seq = [i for i in range(len(priorities))]
    ans = []

    while priorities:
        current = priorities.pop(0)
        s = seq.pop(0)
        if not priorities:
            ans.append(s)
            break
        if current < max(priorities):
            priorities.append(current)
            seq.append(s)
        else:
            ans.append(s)
    answer = ans.index(location) + 1

    return answer


p = [2, 1, 3, 2]
l = 2
p_2 = [1, 1, 9, 1, 1, 1]
l_2 = 0
print(solution(p, l))
print(solution(p_2, l_2))
