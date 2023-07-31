import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

def cal():
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if data[i][j] != 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1

    if count >= 2:
        return True
    else:
        return False

def update_height():
    temp = deque()

    while ices:
        x, y = ices.popleft()
        count = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if data[nx][ny] == 0:
                    count += 1

        temp.append((x, y, count))

    for x, y, count in temp:
        if data[x][y] - count > 0:
            data[x][y] -= count
            ices.append((x, y))
        else:
            data[x][y] = 0

    return cal()

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
answer = 0
ices = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if data[i][j] != 0:
            ices.append((i, j))

while True:
    answer += 1

    if len(ices) == 0:
        print(0)
        break

    if update_height():
        print(answer)
        break

