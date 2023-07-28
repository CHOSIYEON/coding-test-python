import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True
    team = []

    while queue:
        node = queue.popleft()
        team.append(node)

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            else:
                if i in team:
                    return len(team) - team.index(i)
    return 0

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    data = list(map(int, input().split()))
    answer = 0

    for idx, value in enumerate(data):
        graph[idx + 1].append(value)

    for i in range(1, n + 1):
        if not visited[i]:
            answer += bfs(i)

    print(n - answer)

