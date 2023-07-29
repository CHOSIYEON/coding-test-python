import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while tomatoes:
        x, y = tomatoes.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0:
                    data[nx][ny] = data[x][y] + 1
                    tomatoes.append((nx, ny))

m, n = map(int, input().split())
data = []
answer = 0

for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

tomatoes = deque()

for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            tomatoes.append((i, j))

bfs()

for i in data:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)