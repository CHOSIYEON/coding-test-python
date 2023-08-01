import sys
input = sys.stdin.readline

def is_clean(x, y):
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]

        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            return False
    return True

n, m = map(int, input().split())
r, c, d = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
answer = 0

while True:
    if data[r][c] == 0:
        data[r][c] = -1
        answer += 1

    if is_clean(r, c):
        nx = r - dirs[d][0]
        ny = c - dirs[d][1]

        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 1:
            break
        else:
            r, c = nx, ny
    else:
        d = (d + 3) % 4

        nx = r + dirs[d][0]
        ny = c + dirs[d][1]

        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == 0:
            r, c = nx, ny

print(answer)