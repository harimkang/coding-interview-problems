import itertools
import collections


def solution(orders, course):
    max_len = 0
    for o in orders:
        if max_len <= len(o):
            max_len = len(o)
    _temp = course
    for i in range(len(course)):
        if course[i] > max_len:
            _temp = course[:i]
            break
    course = _temp
    answer = []
    menu = ''.join(orders)
    menu = list(set(menu))
    menu.sort()

    container = collections.Counter()
    cand = []
    for o in orders:
        o = ''.join(sorted(list(o)))
        for i in range(2, len(o) + 1):
            cand += list(itertools.combinations(o, i))
    container.update(cand)
    candidate = collections.defaultdict(list)

    for c, v in container.items():
        if v not in course:
            continue
        for i in course:
            if v == i:
                if not candidate[i]:
                    candidate[i].append(len(c))
                    candidate[i].append(''.join(c))
                else:
                    if candidate[i][0] < len(c):
                        candidate[i] = [len(c), ''.join(c)]
                    elif candidate[i][0] == len(c):
                        candidate[i].append(''.join(c))
    for _, value in candidate.items():
        value = value[1:]
        for v in value:
            answer.append(v)

    return sorted(answer)


if __name__ == "__main__":
    # o_1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    # c_1 = [2, 3, 4]
    # print(solution(o_1, c_1))
    o_2 = ["XYZ", "XWY", "WXA"]
    c_2 = [2, 3, 4]
    print(solution(o_2, c_2))