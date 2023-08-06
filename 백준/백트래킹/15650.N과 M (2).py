def dfs(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n + 1):
        if not visited[i]:
            visited[i] = True
            answer.append(i)
            dfs(i)
            answer.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

dfs(1)
