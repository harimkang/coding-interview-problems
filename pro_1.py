def solution(N):
    answer = []

    # N을 k진법으로 수정
    for i in range(1, N + 1):
        rest = []
        temp = N
        while temp >= i:
            _r = temp % i
            _t = temp // i
            rest.append(_r)


if __name__ == "__main__":
    N = 14
    answer = [0, 0]
    for i in range(2, N + 1):
        com = 1
        temp = N
        while temp >= i:
            _r = temp % i
            _t = temp // i
            if _r != 0:
                com *= _r
            temp = _t
        if temp != 0:
            com *= temp

        # com = 1
        # for j in range(len(rest)):
        #     if rest[j] != 0:
        #         com *= rest[j]
        if answer[1] <= com:
            answer = [i, com]

    print(answer)