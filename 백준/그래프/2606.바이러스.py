from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)
    visited[node] = True
    count = 0

    while queue:
        node = queue.popleft()
        count += 1

        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return count


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

print(bfs(1) - 1)
