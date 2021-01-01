def solution(genres, plays):
    song = dict()
    sum_play = dict()
    n = len(genres)
    answer = []

    for i in range(n):
        genre = genres[i]
        num_play = plays[i]
        if genre in song:
            song[genre].append([(-1) * num_play, i])
            song[genre].sort()
        else:
            song[genre] = [[(-1) * num_play, i]]

        if genre in sum_play:
            sum_play[genre] += num_play
        else:
            sum_play[genre] = num_play
    sorted_list = []
    for k in sum_play.keys():
        sorted_list.append([sum_play[k], k])
    sorted_list.sort(reverse=True)

    for _, g in sorted_list:
        for i in range(2):
            answer.append(song[g][i][1])
            if len(song[g]) == 1:
                break
    return answer


gen = ["classic", "pop", "classic", "classic", "pop"]
gen_2 = ["classic", "kpop", "aa", "aa", "kpop"]
play = [500, 600, 150, 800, 2500]
play_2 = [4, 5, 1, 1, 3]
print(solution(gen, play))
print(solution(gen_2, play_2))
