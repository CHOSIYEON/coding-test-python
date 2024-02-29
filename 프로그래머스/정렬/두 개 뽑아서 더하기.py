def solution(numbers):
    answer = set()
    length = len(numbers)

    for i in range(length):
        for j in range(i + 1, length):
            answer.add(numbers[i] + numbers[j])

    answer = sorted(answer)

    return answer