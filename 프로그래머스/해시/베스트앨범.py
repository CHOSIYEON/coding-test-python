def solution(genres, plays):
    answer = []
    length = len(genres)
    albums = {}
    genres_total = {}

    for i in range(length):
        if genres[i] in albums.keys():
            genres_total[genres[i]] += plays[i]
            albums[genres[i]].append([plays[i], i])
        else:
            albums[genres[i]] = [[plays[i], i]]
            genres_total[genres[i]] = plays[i]

    genres_total = sorted(genres_total.items(), key=lambda x: (-x[1]))

    for genre_total in genres_total:
        genre = genre_total[0]
        play = albums[genre]

        if len(play) == 1:
            answer.append(play[0][1])
            continue

        play = sorted(play, key=lambda x: (-x[0], x[1]))

        for i in range(2):
            answer.append(play[i][1])

    return answer