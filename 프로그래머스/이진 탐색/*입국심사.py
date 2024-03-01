# 임의의 시간이 주어졌을 때 몇명을 심사할 수 있는지로 접근함
# 만약 심사할 수 있는 인원이 n보다 많다면 해당 임의의 시간을 줄여서 다시 확인해봄 - 최소 시간을 구해야하니까
# 적다면 해당 임의의 시간으로는 충분하지 않다는 의미이므로 시간을 늘려줘야함

def solution(n, times):
    answer = 0
    left, right = 1, max(times) * n

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += (mid // time)
            if people >= n: break

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer