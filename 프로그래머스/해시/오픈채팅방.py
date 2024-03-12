from collections import defaultdict

def solution(record):
    answer = []
    temp = []
    user_id = defaultdict(str)

    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            uid, nickname = r[1], r[2]
            user_id[uid] = nickname
            temp.append([uid, ' 들어왔습니다.'])
        elif r[0] == 'Leave':
            uid = r[1]
            temp.append([uid, ' 나갔습니다.'])
        elif r[0] == 'Change':
            uid, nickname = r[1], r[2]
            user_id[uid] = nickname

    for r in temp:
        answer.append(user_id[r[0]] + '님이' + r[1])

    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])