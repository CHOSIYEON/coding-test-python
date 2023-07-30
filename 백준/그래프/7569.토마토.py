import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nz, nx, ny = z + dirs[i][0], x + dirs[i][1], y + dirs[i][2]

            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if data[nz][nx][ny] == 0:
                    queue.append((nz, nx, ny))
                    data[nz][nx][ny] = data[z][x][y] + 1


m, n, h = map(int, input().split())

data = []
dirs = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
queue = deque()
answer = -1e9

for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    data.append(temp)

for z in range(h):
    for x in range(n):
        for y in range(m):
            if data[z][x][y] == 1:
                queue.append((z, x, y))

bfs()

for z in range(h):
    for x in range(n):
        if 0 in data[z][x]:
            print(-1)
            exit(0)
        answer = max(answer, max(data[z][x]))
else:
    print(answer - 1)