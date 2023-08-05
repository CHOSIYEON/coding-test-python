import sys
input = sys.stdin.readline

w, n = map(int, input().split())
data = []
answer = 0

for _ in range(n):
    m, p = map(int, input().split())
    data.append((m, p))

data.sort(key = lambda x: x[1], reverse=True)
now = 0

while w != 0:
    if data[now][0] <= w:
        w -= data[now][0]
        answer += (data[now][0] * data[now][1])
        now += 1
    else:
        answer += w * data[now][1]
        break

print(answer)