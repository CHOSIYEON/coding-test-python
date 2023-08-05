import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
answer = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            answer[i] = max(answer[i], answer[j] + 1)

print(max(answer))