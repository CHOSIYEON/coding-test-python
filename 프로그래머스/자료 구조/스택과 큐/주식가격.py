def solution(prices):
    answer = []
    length = len(prices)

    for i in range(length - 1):
        for j in range(i + 1, length):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
        else:
            answer.append(length - i - 1)

    answer.append(0)

    return answer

##########################################
# stack 이용

def solution(prices):
    stack = []
    answer = [0] * len(prices)

    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            past = stack.pop()
            answer[past] = i - past
        stack.append(i)

    for i in stack:
        answer[i] = len(prices) - 1 - i

    return answer