# 정확성 O, 효율성 X
def solution(k, room_numbers):
    answer = []
    rooms = {}

    for room_number in room_numbers:
        if room_number in rooms:
            for rn in range(room_number, k + 1):
                if rn in rooms:
                    continue

                rooms[rn] = 1
                answer.append(rn)
                break
        else:
            rooms[room_number] = 1
            answer.append(room_number)

    return answer

##########################################
# 재귀 호출 횟수 때문에 런타임 에러 발생하므로 import 추가하기

import sys
sys.setrecursionlimit(10 ** 6)

def find_empty_room(n, rooms):
    if n not in rooms:
        rooms[n] = n + 1
        return n

    empty = find_empty_room(rooms[n], rooms)
    rooms[n] = empty + 1
    return empty


def solution(k, room_number):
    answer = []
    rooms = {}

    for n in room_number:
        answer.append(find_empty_room(n, rooms))

    return answer