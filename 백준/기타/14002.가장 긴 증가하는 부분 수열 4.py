n = int(input())
data = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

x = max(dp)
print(x)
answer = []

for i in range(n - 1, -1, -1):
    if dp[i] == x:
        answer.append(data[i])
        x -= 1

print(' '.join(map(str, answer[::-1])))