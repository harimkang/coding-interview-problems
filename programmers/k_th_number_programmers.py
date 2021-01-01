def solution(array, commands):
    def com(arr, a, b, c):
        arr = arr[a - 1 : b]
        arr.sort()
        return arr[c - 1]

    answer = []
    for x, y, z in commands:
        answer.append(com(array, x, y, z))

    return answer


arr1 = [1, 5, 2, 6, 3, 7, 4]
com1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr1, com1))
