def solution(ball, order):
    answer = []
    wl = []

    def ck_wl():
        if ball[0] in wl:
            wl.remove(ball[0])
            answer.append(ball.pop(0))
            ck_wl()
        if ball[-1] in wl:
            wl.remove(ball[-1])
            answer.append(ball.pop())
            ck_wl()

    for _o in order:
        if len(ball) == 1:
            answer.append(ball[0])
            break
        ck_wl()
        if _o == ball[0]:
            answer.append(ball.pop(0))
        elif _o == ball[-1]:
            answer.append(ball.pop())
        else:
            wl.append(_o)
        if len(ball) >= 2:
            ck_wl()

    return answer




if __name__ == "__main__":
    b_1 = [1, 2, 3, 4, 5, 6]
    o_1 = [6, 2, 5, 1, 4, 3]
    print(solution(b_1, o_1))

    b_2 = [11, 2, 9, 13, 24]
    o_2 = [9, 2, 13, 24, 11]
    print(solution(b_2, o_2))