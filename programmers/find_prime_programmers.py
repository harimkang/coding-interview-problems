import itertools


def solution(numbers):
    answer = 0
    numbers = list(numbers)
    p = []
    for i in range(1, len(numbers)+1):
        per = list(itertools.permutations(numbers, i))
        p += per

    px = set([int(''.join(x)) for x in p])
    for s in px:
        ck = False
        if s < 2:
            continue
        for i in range(2, s):
            if s % i == 0:
                ck = True
                break
        if ck:
            continue
        answer += 1
    return answer


tc = ['17', '011']
for c in tc:
    print(solution(c))
