def solution(n):
    n = str(n)
    n = list(map(int, n))

    def progress(_l, count):
        if len(_l) == 1:
            return _l[0], count
        elif len(_l) == 2:
            count += 1
            new = str(_l[0] + _l[1])
            new = list(map(int, new))
            if len(new) == 1:
                return new[0], count
            return progress(new, count)
        count += 1
        a, b = _l[:int(len(_l)/2)], _l[int(len(_l)/2):]
        if b[0] == 0:
            index_a = 0
            index_b = 0
            for i in range(len(a)-1, 0, -1):
                if a[i] != 0:
                    index_a = i
                    break
            for j in range(1, len(b)):
                if b[j] != 0:
                    index_b = j
                    break
            if index_b == 0 or len(a) - index_a < index_b:
                b = a[index_a:] + b
                a = a[:index_a]
            else:
                a = a + b[:index_b]
                b = b[index_b:]
        temp_a = ''.join(list(map(str, a)))
        temp_b = ''.join(list(map(str, b)))
        temp = str(int(temp_a) + int(temp_b))
        new_temp = list(map(int, temp))
        return progress(new_temp, count)

    v, c = progress(n, 0)

    return [c, v]


if __name__ == "__main__":
    n_1 = 73425
    n_2 = 10007
    n_3 = 9
    n_4 = 11100001
    print(solution(n_1))
    print(solution(n_2))
    print(solution(n_3))
    print(solution(n_4))