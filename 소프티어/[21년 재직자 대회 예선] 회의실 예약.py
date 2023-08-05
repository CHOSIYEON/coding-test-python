import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rooms = {}
answers = {}

for _ in range(n):
    room_name = input().rstrip()
    rooms[room_name] = []
    answers[room_name] = []

for _ in range(m):
    r, s, t = input().split()
    rooms[r].append((int(s), int(t)))

for key in rooms.keys():
    rooms[key].sort(key=lambda x: x[0])

for room in rooms.keys():
    now = 9

    for start, end in rooms[room]:
        if now < start:
            answers[room].append((now, start))
        now = end

    if now < 18:
        answers[room].append((now, 18))

answers = sorted(answers.items(), key=lambda x: x[0])

for i in range(len(answers)):
    room_name = answers[i][0]
    times = answers[i][1]

    print('Room %s:' % (room_name))

    if len(times) == 0:
        print('Not available')

        if i != len(answers) - 1:
            print('-----')

        continue
    else:
        print('%d available:' % (len(times)))

    for start, end in times:
        print("%s-%s" % (str(start).zfill(2), str(end).zfill(2)))

    if i != len(answers) - 1:
        print('-----')