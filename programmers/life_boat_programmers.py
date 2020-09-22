
def solution(people, limit):
    answer = 0
    people.sort()
    j = len(people) - 1
    ck = True
    boat = 0
    for i in range(len(people) - 1):
        while j > i:
            if people[j] + people[i] > limit:
                j -= 1
            elif people[j] + people[i] <= limit:
                ck = False
                answer += 1
                boat += 2
                j -= 1
                break
        if ck:
            answer += 1
            boat += 1
    answer += len(people) - boat

    return answer


def solution2(people, limit):
    people.sort()
    answer = 0
    i = 0
    j = len(people) - 1
    while j >= i:
        if people[i] + people[j] <= limit:
            i += 1
        answer += 1
        j -= 1

    return answer



tc = [[[70, 50, 80, 50], 100], [[70, 80, 50], 100], [[20, 50, 50, 80], 100]]
for p2, l2 in tc:
    print(solution2(p2, l2))
