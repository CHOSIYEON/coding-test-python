def dfs(idx):
    if len(answer) == l:
        check(''.join(answer))
        return

    for i in range(idx, c):
        if not visited[i]:
            visited[i] = True
            answer.append(words[i])
            dfs(i)
            answer.pop()
            visited[i] = False

def check(word):
    count = 0

    for w in word:
        if w in ('a', 'i', 'o', 'u', 'e'):
            count += 1

    if count >= 1 and l - count >= 2:
        print(word)

l, c = map(int, input().split())
words = input().split()
visited = [False] * c
answer = []

words.sort()

dfs(0)
