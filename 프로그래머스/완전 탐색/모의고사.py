def solution(answers):
    answer = []
    people = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    max_value = -1

    for p in range(3):
        cnt = 0

        for i in range(len(answers)):
            if answers[i] == people[p][i % len(people[p])]:
                cnt += 1

        if max_value < cnt:
            answer = [p + 1]
            max_value = cnt
        elif max_value == cnt:
            answer.append(p + 1)

        answer = sorted(answer)

    return answer