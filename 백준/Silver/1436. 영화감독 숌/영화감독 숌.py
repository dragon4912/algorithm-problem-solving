import sys
input = sys.stdin.readline

N = int(input().strip())

cnt = 0
iter_val = 666
while(1):
    if '666' in str(iter_val):
        cnt += 1
        if cnt == N:
            answer = iter_val
            break
    iter_val += 1
print(answer)
