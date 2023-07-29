import sys
input = sys.stdin.readline
from collections import deque

k = int(input())

def bfs(node, group):
    queue = deque([node])
    visited[node] = group

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[node] * (-1)
            else:
                if visited[i] == visited[node]:
                    return False
    return True


for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for _ in range(e):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in range(1, v + 1):
        if not visited[i]:
            if not bfs(i, 1):
                print("NO")
                break
    else:
        print("YES")