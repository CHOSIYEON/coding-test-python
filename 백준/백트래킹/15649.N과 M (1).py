def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            dfs()
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

dfs()