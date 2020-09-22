

def solution(numbers):

    answer = ''
    so = []
    for o in numbers:
        o = str(o)
        sz = 12//len(o)
        so.append([o*sz, o])
    so.sort(reverse=True)
    for _, s in so:
        answer += s
    if answer and int(answer) == 0:
        answer = '0'

    return answer


n1 = [6, 10, 2]
n2 = [3, 30, 34, 5, 9]
print(solution(n1))
print(solution(n2))

test_case = [[0, 0, 0, 0, 0], [40, 403], [40, 405],
             [40, 404], [12, 121], [2, 22, 223],
             [21, 212], [41, 415], [2, 22], [70, 0, 0, 0],
             [0, 0, 0, 1000], [12, 1213], [0, 0, 1000, 0],
             [0, 1000, 0, 0], [121, 12], []]
for tc in test_case:
    print(solution(tc))
