from collections import deque
MAX = 100001

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        now = queue.popleft()

        if now == k:
            print(visited[now] - 1)
            break

        for nx in (now * 2, now - 1, now + 1):
            if 0 <= nx < MAX and visited[nx] == 0:
                if nx == now * 2:
                    queue.appendleft(nx)
                    visited[nx] = visited[now]
                else:
                    queue.append(nx)
                    visited[nx] = visited[now] + 1

n, k = map(int, input().split())
visited = [0] * MAX

bfs(n)

# 다른 풀이
# import heapq
#
# def bfs(start):
#     queue = []
#     heapq.heappush(queue, (0, start))
#     visited[start] = True
#
#     while queue:
#         time, now = heapq.heappop(queue)
#
#         if now == k:
#             return time
#
#         for idx, nx in enumerate([now * 2, now + 1, now - 1]):
#             if 0 <= nx <= 100000 and not visited[nx]:
#                 visited[nx] = True
#                 heapq.heappush(queue, (time + times[idx], nx))
#
# n, k = map(int, input().split())
# visited = [False] * 100001
# times = [0, 1, 1]
#
# print(bfs(n))