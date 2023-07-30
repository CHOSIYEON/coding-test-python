import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = 0

    while queue:
        node = queue.popleft()

        if node == p2:
            return visited[node]

        for i in graph[node]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[node] + 1

    return -1

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(p1))