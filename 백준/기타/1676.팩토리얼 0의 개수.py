def factorial(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n * factorial(n - 1)

n = int(input())
answer = str(factorial(n))[::-1]

for i, v in enumerate(answer):
    if v != '0':
        print(i)
        break
