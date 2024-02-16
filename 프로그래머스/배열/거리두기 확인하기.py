def check(matrix):
    people = []

    dx = [-1, 1, 0, 0, -1, -1, 1, 1, 0, 0, 2, -2]
    dy = [0, 0, -1, 1, -1, 1, -1, 1, 2, 2, 0, 0]

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == 'P':
                people.append([i, j])

    for px, py in people:
        # 상하좌우 확인
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and matrix[nx][ny] == 'P':
                print(1)
                return 0

        # 대각선 확인
        for i in range(4, 8):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and matrix[nx][ny] == 'P':
                if matrix[px + dx[i]][py] == 'X' and matrix[px][py + dy[i]] == 'X':
                    continue
                print(2)
                return 0

        # 2칸 상하좌우 확인
        for i in range(8, 12):
            nx = px + dx[i]
            ny = py + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and matrix[nx][ny] == 'P':
                if i <= 9 and matrix[px][py + (dy[i] // 2)] == 'X':
                    continue

                if i > 9 and matrix[px + (dx[i] // 2)][py] == 'X':
                    continue

                return 0

    return 1


def solution(places):
    answer = []

    for place in places:
        answer.append(check(place))

    return answer