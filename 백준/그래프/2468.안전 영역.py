import sys
input = sys.stdin.readline
from collections import deque

def cal_height(height):
    temp = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(n):
            temp[i][j] = data[i][j] - height

            if temp[i][j] < 0:
                temp[i][j] = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and temp[i][j] > 0:
                count += 1
                bfs(i, j, visited, temp)

    return count

def bfs(x, y, visited, temp):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and temp[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
max_height = -1e9
answer = -1e9

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in data:
    max_height = max(max_height, max(i))

for i in range(max_height + 1):
    answer = max(answer, cal_height(i))

print(answer)