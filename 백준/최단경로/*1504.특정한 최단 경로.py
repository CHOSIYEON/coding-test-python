import sys
input = sys.stdin.readline
import heapq
INF = int(1e9)

def dijkstra(start, end):
    distances = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distances[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distances[i[0]] > cost:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distances[end]

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

answer1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n)
answer2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n)

if answer1 >= INF and answer2 >= INF:
    print(-1)
else:
    print(min(answer1, answer2))