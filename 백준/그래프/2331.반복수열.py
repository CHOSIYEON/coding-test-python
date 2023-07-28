a, p = map(int, input().split())
data = [a]
idx = 0

while True:
    temp = sum([pow(int(i), p) for i in str(data[idx])])

    if temp in data:
        print(data.index(temp))
        break

    data.append(temp)
    idx += 1

