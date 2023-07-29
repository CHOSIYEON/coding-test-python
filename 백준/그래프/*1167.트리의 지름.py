import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visited = [-1] * (v + 1)
    visited[node] = 0

    while queue:
        node = queue.popleft()

        for e, d in graph[node]:
            if visited[e] == -1:
                visited[e] = visited[node] + d
                queue.append(e)

    return [visited.index(max(visited)), max(visited)]


v = int(input())
graph = [[] for _ in range(v + 1)]

for _ in range(v):
    data = list(map(int, input().split()))

    for i in range(1, len(data) - 1, 2):
        graph[data[0]].append((data[i], data[i + 1])) # 정점, 거리

max_node = bfs(1)[0]
print(bfs(max_node)[1])