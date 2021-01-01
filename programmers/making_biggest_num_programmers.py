def solution(number, k):
    target = len(number) - k
    if len(number) == 1:
        return number
    number = list(number)
    answer = []
    index = 0
    while True:
        temp_index = 0
        max_v = "-1"
        if k == 0:
            answer.extend(number[index:])
            break
        for i in range(index, index + k + 1):
            if max_v < number[i]:
                max_v = number[i]
                temp_index = i
                if number[i] == "9":
                    break
        answer.append(max_v)
        if len(answer) == target:
            break
        k -= temp_index - index
        index = temp_index + 1
    answer = "".join(answer)
    return answer


tc = [
    ["1924", 2],
    ["1231234", 3],
    ["4177252841", 4],
    ["9999999999999999999999999999999999999989999", 40],
]
for n, c in tc:
    print(solution(n, c))
