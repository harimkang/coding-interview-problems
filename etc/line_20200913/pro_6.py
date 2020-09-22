import collections


def solution(companies, applicants):
    answer = []
    max_len = 0
    company_num_emp = collections.defaultdict(int)
    company_pri = collections.defaultdict(list)
    applicants_pri = collections.defaultdict(list)
    company = collections.defaultdict(list)
    for c in companies:
        c = c.split()
        company_num_emp[c[0]] = int(c[2])
        company_pri[c[0]] = list(c[1])

    for a in applicants:
        a = a.split()
        applicants_pri[a[0]] = list(a[1][:int(a[2])])
        if max_len < len(applicants_pri[a[0]]):
            max_len = len(applicants_pri[a[0]])

    def round_func(app):
        round_dict = collections.defaultdict(list)
        # app: [(지원자, 지원회사)] 리스트
        # app 반복문 돌면서
        for apple, co in app:
            # 지원 접수
            if company_num_emp[co] >= 1:
                round_dict[co].append(apple)

        # 사원이 필요한 company를 돌면서
        for ck in company_num_emp.keys():
            # 선호 인원중에
            for cp in company_pri[ck]:
                # 인원수가 필요하고, 지원자에 선호 인원이 있으면
                if company_num_emp[ck] >= 1 and cp in round_dict[ck]:
                    company_num_emp[ck] -= 1
                    company[ck].append(cp)
                    if applicants_pri[cp]:
                        del applicants_pri[cp]

    for i in range(max_len):
        app_list = []
        for k, v in applicants_pri.items():
            if v:
                app_com = v.pop(0)
                app_list.append([k, app_com])


    return answer


if __name__ == "__main__":
    c_1 = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
    a_1 = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]
    print(solution(c_1, a_1))