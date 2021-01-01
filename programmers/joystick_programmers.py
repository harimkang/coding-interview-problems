def solution(name):
    answer = 0
    front_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    back_alpha = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"]
    back_alpha.reverse()
    not_a_index = 0
    ck = False
    for i in range(len(name)):
        current = name[i]
        if current in front_alpha:
            answer += front_alpha.index(current)
        else:
            answer += back_alpha.index(current)

        if current == "A":
            pass
        else:
            if not_a_index + len(name) - i >= i - not_a_index:
                if ck:
                    continue
                answer += i - not_a_index
            else:
                ck = True
                answer += not_a_index + len(name) - i
            not_a_index = i

    return answer


tc = ["BBBBAAAAAB", "JEROEN", "AZAAAZ", "ABAAAABAB", "ABAAAAAAAAABB"]
for c in tc:
    print(solution(c))
