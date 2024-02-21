def solution(s):
    return (len(s) == 4 or len(s) == 6) and s.isdigit()

##########################################
# 정규식 활용
import re

def solution(s):
    return (len(s) == 4 or len(s) == 6) and bool(re.match('^[0-9]*$', s))


##########################################
# 정규식 활용
# 문자열 길이 조건 추가
def solution(s):
    return bool(re.match('^(\d{4}|\d{6})$', s))
