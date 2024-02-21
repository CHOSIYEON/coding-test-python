def solution(n):
    answer = 0
    base3 = []

    while n > 0:
        n, r = divmod(n, 3)
        base3.append(r)

    for i in range(len(base3)):
        answer += base3[i] * pow(3, len(base3) - i - 1)

    return answer

