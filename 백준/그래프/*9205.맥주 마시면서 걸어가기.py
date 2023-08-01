import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    queue = deque()
    queue.append((home_x, home_y))

    while queue:
        x, y = queue.popleft()

        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return "happy"
        for i in range(n):
            if not visited[i]:
                store_x, store_y = stores[i]
                if abs(x - store_x) + abs(y - store_y) <= 1000:
                    visited[i] = True
                    queue.append((store_x, store_y))

    return "sad"

t = int(input())

for _ in range(t):
    n = int(input())
    stores = []

    home_x, home_y = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())
        stores.append((x, y))

    festival_x, festival_y = map(int, input().split())
    visited = [False] * n

    print(bfs())

