import sys
input = sys.stdin.readline
import heapq

INF = int(1e9)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]
distances = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, v + 1):
    if distances[i] == INF:
        print('INF')
    else:
        print(distances[i])