def solution(brown, red):
    answer = [0, 0]
    for i in range(1, red + 1):
        width, height = red // i, i
        if width < height:
            break
        if red % i != 0:
            continue
        if (width + 2) * (height + 2) == brown + red:
            answer = [width + 2, height + 2]
    return answer


tc = [[10, 2], [8, 1], [24, 24]]
for b, r in tc:
    print(solution(b, r))
