import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)

    visited = [-1] * (n + 1)
    visited[node] = 0

    while queue:
        node = queue.popleft()

        for node2, dist in graph[node]:
            if visited[node2] == -1:
                visited[node2] = visited[node] + dist
                queue.append(node2)

    return [visited.index(max(visited)), max(visited)]

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    node1, node2, dist = map(int, input().split())
    graph[node1].append((node2, dist))
    graph[node2].append((node1, dist))

max_node = bfs(1)[0]
print(bfs(max_node)[1])