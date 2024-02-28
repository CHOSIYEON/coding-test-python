import math

def solution(brown, yellow):
    width = math.ceil((brown - 4) / 4) + 2
    height = math.floor((brown - 4) / 4) + 2

    while True:
        if (width - 2) * (height - 2) == yellow:
            return [width, height]
            break
        else:
            width += 1
            height -= 1

    return answer