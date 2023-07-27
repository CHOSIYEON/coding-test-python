import sys
from itertools import combinations
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y, = y, x % y
    return x

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    answer = []
    candidates = list(combinations(data[i][1:], 2))

    for x, y in candidates:
        answer.append(gcd(x, y))

    print(sum(answer))