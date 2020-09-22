def solution(arrangement):
    answer = 0
    bar = [1]
    for i in range(1, len(arrangement)):
        if arrangement[i] == '(':
            bar.append(1)
        elif arrangement[i] == ')':
            if arrangement[i-1] == '(':
                bar.pop(-1)
                if bar:
                    answer += sum(bar)
                # 이때는 레이저
            else:
                answer += bar.pop(-1)

    return answer


arr = '()(((()())(())()))(())'
print(solution(arr))