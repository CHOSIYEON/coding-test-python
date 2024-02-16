def solution(n):
    answer = []

    matrix = [[0] * n for _ in range(n)]
    directions = [(1, 0), (0, 1), (-1, -1)]

    d = 0
    now = 0
    x, y = -1, 0

    for count in range(n, 0, -1):
        for _ in range(count):
            now += 1

            nx = x + directions[d][0]
            ny = y + directions[d][1]

            matrix[nx][ny] = now

            x, y = nx, ny

        d = (d + 1) % 3

    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                answer.append(matrix[i][j])

    return answer