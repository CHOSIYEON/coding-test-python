import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True
    path = []

    while queue:
        node = queue.popleft()
        path.append(node)

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    if path[0] in graph[path[-1]]:
        return True
    else:
        return False

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] *  (n + 1)
    data = list(map(int, input().split()))
    answer = 0

    for idx, value in enumerate(data):
        graph[idx + 1].append(value)

    for i in range(1, n + 1):
        if not visited[i]:
            if bfs(i):
                answer += 1

    print(answer)