import sys
input = sys.stdin.readline

def dfs(idx, sum_value):
    global answer

    if idx >= n:
        return

    sum_value += data[idx]

    if sum_value == s:
        answer += 1

    dfs(idx + 1, sum_value)
    dfs(idx + 1, sum_value - data[idx])


n, s = map(int, input().split())
data = list(map(int, input().split()))
answer = 0

dfs(0, 0)
print(answer)
