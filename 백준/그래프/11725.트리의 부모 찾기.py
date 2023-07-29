import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def dfs(node):
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            answer.append((i, node))
            dfs(i)

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
answer = []

for _ in range(n - 1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(1)
answer.sort()

for i in answer:
    print(i[1])

# BFS
# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def bfs(node):
#     queue = deque()
#     queue.append(node)
#     visited[node] = True
#
#     while queue:
#         node = queue.popleft()
#
#         for i in graph[node]:
#             if not visited[i]:
#                 answer.append((i, node))
#                 visited[i] = True
#                 queue.append(i)
#
#
# n = int(input())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# answer = []
#
# for _ in range(n - 1):
#     node1, node2 = map(int, input().split())
#     graph[node1].append(node2)
#     graph[node2].append(node1)
#
# bfs(1)
# answer.sort()
#
# for i in answer:
#     print(i[1])