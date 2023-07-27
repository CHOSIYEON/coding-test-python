import sys
input = sys.stdin.readline

def isPrime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())
data = list(map(int, input().split()))
answer = 0

for num in data:
    if isPrime(num):
        answer += 1

print(answer)

