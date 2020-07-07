# 생각보다 쉽지 않았던 문제..
# 검색이용해서 해결,,

def solution(genres, plays):
    answer = []
    playlist = dict()
    playNum = []
    for idx, item in enumerate(genres):
        if item not in playlist:
            playlist[item] = []

        playlist[item].append((idx, plays[idx]))

    for i in playlist.keys():
        playlist[i].sort(key=lambda x: x[1], reverse=True)

    playNum = sorted(playlist.values(), key=lambda x: sum(i[1] for i in x), reverse=True)

    for i in playNum:
        if len(i) == 1:
            answer.append(i[0][0])
        else:
            answer.append(i[0][0])
            answer.append(i[1][0])

    return answer


solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500])
