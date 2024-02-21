def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1
        answer[1] += s.count('0')
        s = s.replace('0', '')
        n = len(s)
        nums = []

        while n > 0:
            n, r = divmod(n, 2)
            nums.append(str(r))

        nums = ''.join(nums[::-1])
        s = nums


    return answer

##########################################
## 속도는 위 풀이보단 느림
## bin() - 10진수를 2진수로 변환

def solution(s):
    cnt, cnt_zero = 0, 0

    while len(s) != 1:
        cnt += 1
        cnt_zero += s.count('0')
        s = s.replace('0', '')
        s = str(bin(len(s)))[2:]

    return [cnt, cnt_zero]
