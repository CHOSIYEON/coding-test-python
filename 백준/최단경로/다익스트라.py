import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 최댓값 설정

def dijkstra(start):
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

n, m = map(int, input().split()) # 노드 n개, 간선 m개
start = int(input())
graph = [[] for i in range(n + 1)]
distances = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split()) # a -> b로 갈 때 거리 c
    graph[a].append((b, c))

dijkstra(start)

for i in range(1, n + 1):
    if distances[i] == INF:
        print("INFINITY")
    else:
        print(distances[i])