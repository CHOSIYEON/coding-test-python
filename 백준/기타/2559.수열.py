import sys
input = sys.stdin.readline

# 시간 초과
# n, k = map(int, input().split())
# data = list(map(int, input().split()))
# answer = []
#
# for i in range(n - k + 1):
#     answer.append(sum(data[i:i + k]))
#
# print(max(answer))

n, k = map(int, input().split())
data = list(map(int, input().split()))
answer = []
answer.append(sum(data[:k]))

for i in range(n - k):
    answer.append(answer[i] - data[i] + data[i + k])

print(max(answer))