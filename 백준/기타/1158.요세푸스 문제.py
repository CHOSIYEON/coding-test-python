n, k = map(int, input().split())

data = [i for i in range(1, n + 1)]
answer = []  # 제거된 사람들을 넣을 배열
idx = 0  # 제거될 사람의 인덱스 번호

for i in range(n):
    idx += k - 1

    if idx >= len(data):
        idx %= len(data)

    answer.append(data.pop(idx))

print("<", ", ".join(map(str, answer))[:], ">", sep='')