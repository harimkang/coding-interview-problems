def solution(boxes):
    temp = []
    for a, b in boxes:
        if a in temp:
            temp.remove(a)
        else:
            temp.append(a)
        if b in temp:
            temp.remove(b)
        else:
            temp.append(b)
    return int(len(temp)/2)


if __name__ == "__main__":
    ex_1 = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
    print(solution(ex_1))

    ex_2 = [[1, 2], [3, 4], [5, 6]]
    print(solution(ex_2))

    ex_3 = [[1, 2], [2, 3], [3, 1]]
    print(solution(ex_3))