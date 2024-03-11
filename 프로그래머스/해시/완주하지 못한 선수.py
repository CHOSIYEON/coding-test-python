from collections import defaultdict

def solution(participant, completion):
    p_dict, c_dict = defaultdict(int), defaultdict(int)

    for p in participant:
        p_dict[p] += 1

    for c in completion:
        c_dict[c] += 1

    for p in participant:
        if p in c_dict and p_dict[p] == c_dict[p]:
            continue
        return p

##########################################
# Counter 사용
from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return [key for key in answer.keys()][0]

##########################################
# hash 이용
def solution(participant, completion):
    value = 0
    answer = {}

    for part in participant:
        answer[hash(part)] = part
        value += int(hash(part))

    for comp in completion:
        value -= int(hash(comp))

    return answer[value]