def changeWord(word):
    changed = ''

    for i in range(len(word)):
        if i % 2 == 0:
            changed += word[i].upper()
        else:
            changed += word[i].lower()

    return changed


def solution(s):
    answer = ''
    string = ''

    for char in s:
        if char.isalpha():
            string += char
        else:
            answer += changeWord(string)
            answer += ' '
            string = ''

    if string:
        answer += changeWord(string)

    return answer

##########################################

def solution(s):
    answer = ''
    count = 0

    for i in range(len(s)):
        if s[i].isalpha():
            answer += s[i].upper() if count % 2 == 0 else s[i].lower()
            count += 1
        else:
            answer += s[i]
            count = 0

    return answer