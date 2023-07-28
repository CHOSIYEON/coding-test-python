import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = 0

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        answer += 1

print(answer)
