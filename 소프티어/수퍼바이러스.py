import sys
input = sys.stdin.readline

def cal(x, y):
    if y == 1:
        return x
    elif y % 2 == 0:
        a = cal(x, y / 2)
        return a * a % 1000000007
    else:
        b = cal(x, (y - 1) / 2)
        return b * b * x % 1000000007

k, p, n = map(int, input().split())

n = 10 * n
answer = cal(p, n)
answer *= k

print(answer % 1000000007)
