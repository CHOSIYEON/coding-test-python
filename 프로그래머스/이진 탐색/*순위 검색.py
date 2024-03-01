# 시간 초과
def solution(info, queries):
    answer = []
    info = [x.split() for x in info]

    for query in queries:
        query = query.split()

        for _ in range(3):
            query.remove('and')

        cnt = 0
        for i in info:
            for j in range(4):
                if query[j] == '-':
                    continue
                elif query[j] != i[j]:
                    break
            else:
                if int(i[-1]) >= int(query[-1]):
                    cnt += 1

        answer.append(cnt)
    return answer

## 정답

from itertools import combinations
from collections import defaultdict

def find_left_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1

    return left


def solution(info, query):
    answer = []
    people = defaultdict(list)

    for i in info:
        person = i.split()
        score = int(person.pop())

        people[''.join(person)].append(score)

        for j in range(4):
            case = list(combinations(person, j))

            for c in case:
                people[''.join(c)].append(score)

    for i in people:
        people[i].sort()

    for q in query:
        key = q.split()
        score = int(key.pop())
        key = ''.join(key)
        key = key.replace('and', '').replace(' ', '').replace('-', '')

        answer.append(len(people[key]) - find_left_bound(people[key], score))

    return answer