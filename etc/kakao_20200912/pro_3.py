import pandas as pd


def solution(info, query):
    answer = []
    df = pd.DataFrame(columns=['lan', 'end', 'car', 'food', 'score'])
    for i in range(len(info)):
        temp = info[i].split()
        temp[-1] = int(temp[-1])
        df.loc[i] = temp

    def solv(_l, e, c, f, s):
        ck_score = df['score'] >= int(s)
        new_df = df[ck_score]
        if _l != '-':
            ck_lan = new_df['lan'] == _l
            new_df = new_df[ck_lan]
        if e != '-':
            ck_end = new_df['end'] == e
            new_df = new_df[ck_end]
        if c != '-':
            ck_car = new_df['car'] == c
            new_df = new_df[ck_car]
        if f != '-':
            ck_food = new_df['food'] == f
            new_df = new_df[ck_food]
        return new_df.shape[0]

    for q in query:
        t = q.split()
        pro_info = t[:-1]
        score = t[-1]
        pro_info = pro_info[::2]
        answer.append(solv(pro_info[0], pro_info[1], pro_info[2], pro_info[3], score))

    return answer


if __name__ == "__main__":
    _info = ["java backend junior pizza 150", "python frontend senior chicken 210",
             "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80",
             "python backend senior chicken 50"]
    _query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
              "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
              "- and - and - and chicken 100", "- and - and - and - 150"]
    print(solution(_info, _query))
