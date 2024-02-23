from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    all_numbers = set()

    for i in range(1, len(numbers) + 1):
        _numbers = list(permutations(numbers, i))

        for n in _numbers:
            all_numbers.add(int(''.join(n)))

    for an in all_numbers:
        if is_prime(an):
            answer += 1

    return answer