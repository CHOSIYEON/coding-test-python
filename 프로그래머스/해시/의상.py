from collections import defaultdict

def solution(clothes):
    answer = 1
    all_clothes = defaultdict(list)

    for cloth in clothes:
        name, kind = cloth
        all_clothes[kind].append(name)

    for key in all_clothes.keys():
        answer *= (len(all_clothes[key]) + 1)

    return answer - 1
