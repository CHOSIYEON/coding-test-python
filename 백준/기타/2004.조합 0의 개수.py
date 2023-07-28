def count(n, c):
    count = 0
    while n != 0:
        n = n // c
        count += n
    return count

n, m = map(int, input().split())
answer = min(count(n, 2) - count(n - m, 2) - count(m, 2), count(n, 5) - count(n - m, 5) - count(m, 5))
print(answer)

