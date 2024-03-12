import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    times = deque()

    for i in range(len(progresses)):
        times.append(math.ceil((100 - progresses[i]) / speeds[i]))

    before = times.popleft()
    count = 1

    while times:
        _next = times.popleft()

        if _next <= before:
            count += 1
        else:
            answer.append(count)
            before = _next
            count = 1

    answer.append(count)

    return answer