from collections import deque

def bfs():
    queue = deque()
    queue.append((n, 0))
    visited[n] = True

    while queue:
        now, time = queue.popleft()

        if now == k:
            return time

        for nx in (now - 1, now + 1, now * 2):
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

n, k = map(int, input().split())
visited = [False] * 100001

print(bfs())

# from collections import deque
#
# n, k = map(int, input().split())
# queue = deque()
# queue.append(n)
# dist = [0] * 100001
#
# while queue:
#     now = queue.popleft()
#
#     if now == k:
#         print(dist[now])
#         break
#
#     for nx in (now + 1, now - 1, now * 2):
#         if 0 <= nx < 100001 and not dist[nx]:
#             dist[nx] = dist[now] + 1
#             queue.append(nx)
