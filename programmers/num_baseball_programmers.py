def solution(baseball):
    answer = 0
    for i in range(111, 1000):
        comp = str(i)
        ck = True
        if '0' in comp or comp[0] == comp[1] or comp[1] == comp[2] or comp[0] == comp[2]:
            continue
        for a, strike, ball in baseball:
            a = str(a)
            t = [0, 1, 2]
            for j in range(3):
                if comp[j] == a[j]:
                    strike -= 1
                    t.remove(j)
                    continue
                else:
                    for k in t:
                        if comp[j] == a[k]:
                            ball -= 1
                            break

            if strike != 0 or ball != 0:
                ck = False
                break
        if ck:
            answer += 1

    return answer


tc = [[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]]
for c in tc:
    print(solution(c))