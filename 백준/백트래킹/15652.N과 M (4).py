def dfs(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n + 1):
        answer.append(i)
        dfs(i)
        answer.pop()

n, m = map(int, input().split())
answer = []

dfs(1)
