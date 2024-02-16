def solution(s, n):
    answer = ''

    for char in s:
        _origin = ord(char)
        _next = ord(char) + n

        if 65 <= _origin <= 90:
            if 65 <= _next <= 90:
                answer += chr(_next)
            else:
                answer += chr(_next - 26)

        elif 97 <= _origin <= 122:
            if 97 <= _next <= 122:
                answer += chr(_next)
            else:
                answer += chr(_next - 26)

        else:
            answer += char

    return answer