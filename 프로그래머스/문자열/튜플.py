def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    sorted_s = []

    for num in s:
        num = num.split(',')
        sorted_s.append(num)

    sorted_s.sort(key=lambda x: len(x))

    for num in sorted_s:
        for n in num:
            if int(n) in answer:
                continue

            answer.append(int(n))

    return answer


##########################################
# 최적화
def solution(s):
    answer = {} # 존재 여부를 확인할 때 in, not in 는 O(1)으로 훨씬 적게 걸림
    s = sorted(s[2:-2].split('},{'), key=len)

    for tuple in s:
        els = tuple.split(',')

        for el in els:
            num = int(el)

            if num in answer:
                continue

            answer[num] = 1

    return list(answer) # key 값만 리스트로 반환

##########################################
# eval 사용
# eval - 문자열로 식을 입력하면 해당식을 실행한 결과값을 반환
def solution(s):
    answer = {}
    s = eval(s.replace("{", "[").replace("}", "]"))
    s.sort(key=len)

    for i in s:
        for j in i:
            if int(j) in answer:
                continue
            answer[int(j)] = 1

    return list(answer)