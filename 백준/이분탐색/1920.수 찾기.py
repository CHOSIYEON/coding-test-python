import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

data.sort()

for number in numbers:
    start, end = 0, n-1
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == number:
            answer = 1
            break
        elif data[mid] < number:
            start = mid + 1
        else:
            end = mid - 1

    print(answer)