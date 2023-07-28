import sys
input = sys.stdin.readline

prime = [1] * 1000001

for i in range(3, int(1000001 ** 0.5) + 1):
    if prime[i]:
        for j in range(i * 2, 1000001, i):
            prime[j] = 0

while True:
    n = int(input())

    if n == 0:
        break

    for i in range(3, int(n / 2) + 1, 2):
        if prime[i] and prime[n - i]:
            print("%d = %d + %d"%(n, i, n - i))
            break
    else:
        print("Goldbach's conjecture is wrong.")