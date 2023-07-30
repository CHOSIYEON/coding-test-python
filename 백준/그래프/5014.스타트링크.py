from collections import deque

def bfs():
    queue = deque()
    queue.append((s, 0))

    while queue:
        now, time = queue.popleft()

        if now == g:
            return time

        for nx in (now + u, now - d):
            if 1 <= nx <= f and not visited[nx]:
                visited[nx] = True
                queue.append((nx, time + 1))

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
visited = [False] * (f + 1)

print(bfs())