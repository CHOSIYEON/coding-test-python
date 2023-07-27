n, b = map(int, input().split())
data = {i: chr(i + 55) for i in range(10, 36)}
answer = ''

q = n

while q:
    q, r = q // b, q % b

    if r >= 10:
        answer += data[r]
    else:
        answer += str(r)

print(''.join(answer[::-1]))