import sys
input = sys.stdin.readline

answer = 0

for i in range(5):
    start, end = input().split()

    start_hour = int(start[:2])
    start_minute = int(start[3:])
    end_hour = int(end[:2])
    end_minute = int(end[3:])

    answer += (end_hour * 60 + end_minute) - (start_hour * 60 + start_minute)

print(answer)