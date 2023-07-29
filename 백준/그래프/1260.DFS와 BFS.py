import sys
input = sys.stdin.readline
from collections import deque

def dfs(node):
    visited[node] = True
    print(node, end=' ')

    for i in graph[node]:
        if not visited[i]:
            dfs(i)

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True

    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

dfs(v)
visited = [False] * (n + 1)
print()
bfs(v)

