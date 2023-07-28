import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    data[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w:
                if data[nx][ny] == 1:
                    queue.append((nx, ny))
                    data[nx][ny] = 0


dx = [-1, 1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    data = []
    answer = 0
    for _ in range(h):
        data.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if data[i][j] == 1:
                answer += 1
                bfs(i, j)

    print(answer)