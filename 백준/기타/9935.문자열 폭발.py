data = input().rstrip()
explore = input().rstrip()

answer = []

for i in data:
    answer.append(i)

    if i == explore[-1] and ''.join(answer[-len(explore):]) == explore:
        # 시간 초과
        # answer = answer[:len(answer) - len(explore)]

        # 통과
        # for _ in range(len(explore)):
        #     answer.pop()

        # 통과
        del answer[-len(explore):]

answer = ''.join(answer)

if answer:
    print(answer)
else:
    print('FRULA')

# 시간 초과
# from collections import deque
#
# queue = deque()
# data = input().rstrip()
# explore = input()
# answer = ''
#
# for i in data:
#     queue.append(i)
#
# while queue:
#     answer += queue.popleft()
#
#     if explore in answer:
#         answer = answer.replace(explore, '')
#
# if len(answer) == 0:
#     print('FRULA')
# else:
#     print(answer)

