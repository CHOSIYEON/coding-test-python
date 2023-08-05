import sys
input = sys.stdin.readline

m, n, k = map(int, input().split())
secrets = "".join(list(map(str,input().split())))
user = "".join(list(map(str,input().split())))

if n < m:
    print('normal')
else:
    if secrets in user:
        print('secret')
    else:
        print('normal')
