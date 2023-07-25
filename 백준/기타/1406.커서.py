import sys
from collections import deque
input = sys.stdin.readline

data = input().rstrip()

queue1 = deque()
queue2 = deque()

n = int(input())

for d in data:
    queue1.append(d)

for _ in range(n):
    cmds = input().split()

    if cmds[0] == 'P':
        queue1.append(cmds[1])
    elif cmds[0] == 'L':
        if queue1:
            queue2.appendleft(queue1.pop())
    elif cmds[0] == 'D':
        if queue2:
            queue1.append(queue2.popleft())
    else:
        if queue1:
            queue1.pop()


print(''.join(queue1), ''.join(queue2), sep='')


