def solution(rows, columns, queries):
    answer = []

    matrix = [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:

        tmp = matrix[x1 - 1][y1 - 1]
        min_value = int(1e9)

        for y in range(y1, y2):
            min_value = min(min_value, tmp)
            matrix[x1 - 1][y], tmp = tmp, matrix[x1 - 1][y]

        for x in range(x1, x2):
            min_value = min(min_value, tmp)
            matrix[x][y2 - 1], tmp = tmp, matrix[x][y2 - 1]

        for y in range(y2 - 2, y1 - 2, -1):
            min_value = min(min_value, tmp)
            matrix[x2 - 1][y], tmp = tmp, matrix[x2 - 1][y]

        for x in range(x2 - 2, x1 - 2, -1):
            min_value = min(min_value, tmp)
            matrix[x][y1 - 1], tmp = tmp, matrix[x][y1 - 1]

        answer.append(min_value)

    return answer