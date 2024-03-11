def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance

    rocks.sort()
    rocks.append(end)

    while start <= end:
        mid = (start + end) // 2
        removed = 0
        temp = 0

        for rock in rocks:
            if rock - temp < mid:
                removed += 1
            else:
                temp = rock

            if removed > n:
                break

        if removed > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer