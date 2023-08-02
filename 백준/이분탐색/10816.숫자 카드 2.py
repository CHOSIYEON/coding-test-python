# 방법 1
# import sys
# input = sys.stdin.readline
# from collections import defaultdict
#
# n = int(input())
# data = list(map(int, input().split()))
# m = int(input())
# numbers = list(map(int, input().split()))
#
# checked = defaultdict(int)
#
# for i in data:
#     checked[i] += 1
#
# for number in numbers:
#     print(checked[number], end=' ')

# 방법 2
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

def find_number(number):
    start_index = bisect_left(data, number)
    end_index = bisect_right(data, number)
    return end_index - start_index

n = int(input())
data = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

data.sort()

for number in numbers:
    print(find_number(number), end=' ')


