def solution(lines):
    answer = []
    pos = []
    length = len(lines)

    x_min, x_max = int(1e15), -int(1e15)
    y_min, y_max = int(1e15), -int(1e15)

    for i in range(length):
        a, b, e = lines[i]

        for j in range(i + 1, length):
            c, d, f = lines[j]

            if a * d == b * c:
                continue

            x = ((b * f) - (e * d)) / ((a * d) - (b * c))
            y = ((e * c) - (a * f)) / ((a * d) - (b * c))

            if (x == int(x) and y == int(y)):
                x, y = int(x), int(y)
                pos.append([x, y])

                if x_min > x: x_min = x
                if x_max < x: x_max = x
                if y_min > y: y_min = y
                if y_max < y: y_max = y

    row = x_max - x_min + 1
    col = y_max - y_min + 1

    coord = [['.'] * row for _ in range(col)]

    for x, y in pos:
        nx = x + abs(x_min) if x_min < 0 else x - x_min
        ny = y + abs(y_min) if y_min < 0 else y - y_min

        coord[ny][nx] = '*'

    for c in coord:
        answer.append(''.join(c))

    return answer[::-1]