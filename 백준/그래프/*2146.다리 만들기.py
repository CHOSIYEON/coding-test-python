from collections import deque

def bfs(x, y, group):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
                queue.append([nx, ny])
                data[nx][ny] = group


def cal_distance(group):
    distances = [[-1] * n for _ in range(n)]
    queue = deque()

    for i in range(n):
        for j in range(n):
            if data[i][j] == group:
                queue.append([i, j])
                distances[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 다른 섬 도착
                if data[nx][ny] > 0 and data[nx][ny] != group:
                    return distances[x][y]
                # 바다
                if data[nx][ny] == 0 and distances[nx][ny] == -1:
                    distances[nx][ny] = distances[x][y] + 1
                    queue.append([nx, ny])

    return 1e9


n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
group = 2
answer = 1e9

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            data[i][j] = group
            bfs(i, j, group)
            group += 1

for i in range(2, group + 1):
    answer = min(answer, cal_distance(i))

print(answer)

# 메모리 초과
# import sys
# input = sys.stdin.readline
# from collections import deque
# from itertools import combinations
#
# def bfs(x, y):
#     queue = deque()
#     queue.append((x, y))
#     island = []
#
#     while queue:
#         x, y = queue.popleft()
#         island.append((x, y))
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < n:
#                 if data[nx][ny] == 1:
#                     queue.append((nx, ny))
#                     data[nx][ny] = 0
#
#     return island
#
# def cal_distance(candidate):
#     a, b = candidate
#     distances = []
#
#     for x, y in islands[a]:
#         for x2, y2 in islands[b]:
#             distances.append(abs(x - x2) + abs(y - y2))
#
#     return min(distances)
#
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# islands = []
# answer = 1e9
#
# for i in range(n):
#     for j in range(n):
#         if data[i][j] == 1:
#             islands.append(bfs(i, j))
#
# candidates = list(combinations([i for i in range(len(islands))], 2))
#
# for candidate in candidates:
#     answer = min(answer, cal_distance(candidate))
#
# print(answer - 1)
