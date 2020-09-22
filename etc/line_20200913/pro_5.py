def solution(cards):
    money = 0

    def get_card():
        if cards:
            card = cards.pop(0)
            if card > 10:
                card = 10
            return card

    def get_result(p, d):
        d = ck_one(d, 17)
        while sum(d) < 17:
            if not cards:
                return 'Draw'
            card = get_card()
            d.append(card)
            d = ck_one(d, 17)
        if sum(p) > 21:
            return 'D'
        if sum(d) > 21:
            return 'P'
        if sum(p) > sum(d):
            if sum(p) == 21:
                return 'B'
            return 'P'
        elif sum(p) == sum(d):
            return 'Draw'
        else:
            return 'D'

    def ck_one(p, n):
        temp = []
        for i in range(len(p)):
            if p[i] == 1 and n < sum(p) + 10 <= 21:
                temp.append(11)
            else:
                temp.append(p[i])
        return temp

    def progress_game():
        player = []
        dealer = []
        # card 두장 분배 1~4
        for i in range(2):
            first = get_card()
            second = get_card()
            player.append(first)
            dealer.append(second)
        player = ck_one(player, 17)
        dealer = ck_one(dealer, 17)

        if not cards:
            return 0
        # 블랙잭 체크
        if sum(player) == 21 and sum(dealer) < 21:
            return 'B'

        if dealer[1] in [1, 7]:
            player = ck_one(player, 17)
            while sum(player) < 17:
                if not cards:
                    return 'Draw'
                card = get_card()
                player.append(card)
                player = ck_one(player, 17)
        elif dealer[1] in [4, 5, 6]:
            return get_result(player, dealer)
        elif dealer[1] in [2, 3]:
            while sum(player) < 12:
                if not cards:
                    return 'Draw'
                card = get_card()
                player.append(card)
                player = ck_one(player, 17)
        return get_result(player, dealer)

    while len(cards) >= 4:
        result = progress_game()
        if result == 'P':
            money += 2
        elif result == 'Draw':
            continue
        elif result == 'B':
            money += 3
        else:
            money -= 2

    return money


if __name__ == "__main__":
    c_1 = [12, 7, 11, 6, 2, 12]
    print(solution(c_1))

    c_2 = [1, 4, 10, 6, 9, 1, 8, 13]
    print(solution(c_2))

    c_3 = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
    print(solution(c_3))

    c_4 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    print(solution(c_4))