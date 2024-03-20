from collections import deque

def bfs(node, graph, distances):
    queue = deque()
    queue.append(node)
    distances[node] = 0

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if distances[i] == -1:
                queue.append(i)
                distances[i] = distances[node] + 1

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distances = [-1 for _ in range(n + 1)]

    for node1, node2 in edge:
        graph[node1].append(node2)
        graph[node2].append(node1)

    bfs(1, graph, distances)
    max_value = max(distances)
    return distances.count(max_value)