from itertools import permutations
from collections import deque

def calculate(tokens_ori, priority):
    tokens = tokens_ori.copy()

    for p in priority:
        stack = []
        while tokens:
            token = tokens.popleft()
            if token == p:
                a = stack.pop()
                b = tokens.popleft()

                stack.append(str(eval(a + token + b)))
            else:
                stack.append(token)

        tokens = deque(stack)
    return abs(int(stack[0]))


def solution(expression):
    answer = 0
    priority = list(permutations(['*', '-', '+'], 3))
    tokens, num = deque(), ''

    for e in expression:
        if e.isdigit():
            num += e
        else:
            tokens.append(num)
            tokens.append(e)
            num = ''

    tokens.append(num)

    for p in priority:
        answer = max(answer, calculate(tokens, p))

    return answer