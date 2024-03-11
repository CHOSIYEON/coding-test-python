def solution(phone_book):
    phone_book.sort()
    length = len(phone_book)

    for i in range(length - 1):
        if phone_book[i] in phone_book[i + 1][:len(phone_book[i])]:
            return False

    return True

##########################################
# hash 이용

def solution(phone_book):
    headers = dict()

    for pb in phone_book:
        headers[pb] = 1

    for pb in phone_book:
        header = ''
        for n in pb:
            header += n

            if header in headers and header != pb:
                return False
    return True