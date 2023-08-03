import sys
input = sys.stdin.readline
from collections import deque

def move():
    while fireballs:
        r, c = fireballs.popleft()
        m, s, d = data[r][c].popleft()

        nr = (r + dirs[d][0] * s) % n
        nc = (c + dirs[d][1] * s) % n

        data[nr][nc].append(deque((m, s, d)))

    for i in range(n):
        for j in range(n):
            if len(data[i][j]) >= 2:
                mass, speed = 0, 0
                count = [0, 0]
                length = len(data[i][j])

                while data[i][j]:
                    m, s, d = data[i][j].popleft()
                    mass += m
                    speed += s
                    count[d % 2] += 1

                if mass // 5 == 0:
                    continue

                if count[0] * count[1] == 0:
                    directions = [0, 2, 4, 6]
                else:
                    directions = [1, 3, 5, 7]

                for direction in directions:
                    fireballs.append((i, j))
                    data[i][j].append(deque((mass // 5, speed // length, direction)))
            elif len(data[i][j]) == 1:
                fireballs.append((i, j))

n, m, k = map(int, input().split())
fireballs = deque()
dirs = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
data = [[deque() for _ in range(n)] for _ in range(n)]
answer = 0

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1))
    data[r - 1][c - 1].append((deque((m, s, d))))

for _ in range(k):
    move()

for i in range(n):
    for j in range(n):
        answer += sum(arr[0] for arr in data[i][j])

print(answer)

