# 재귀
# def find(data, p, step): # 사전을 기록할 배열, 현재 문자열, 현재 문자열 숫자
#     if step == 6:
#         return
#
#     if p != '':
#         data.append(p)
#
#     for c in ['A', 'E', 'I', 'O', 'U']:
#         find(data, ''.join([p, c]), step + 1)
#
# def solution(word):
#     data = []
#     find(data, '', 0)
#
#     for i in range(len(data)):
#         if data[i] == word:
#             return i + 1

##########################################
# 단어의 위치를 알아내서 직접 계산

def solution(word):
    preset = {
        'A': [1, 1, 1, 1, 1],
        'E': [782, 157, 32, 7, 2],
        'I': [1563, 313, 63, 13, 3],
        'O': [2344, 469, 94, 19, 4],
        'U': [3125, 625, 125, 25, 5]
    }

    answer = 0

    for idx, value in enumerate(word):
        answer += preset[value][idx]

    return answer


solution('AAAE')