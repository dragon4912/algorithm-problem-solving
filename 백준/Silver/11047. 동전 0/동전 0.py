import sys
input = sys.stdin.readline

N, K = map(int, input().split())        #가로 수, 세로 수

A = []
for _ in range(N):
    A.append(int(input().strip()))
A.sort(reverse=True)

answer = 0
for a in A:
    if a <= K:
        cnt = K // a
        answer += cnt
        K = K % a

        if K == 0:
            break
print(answer)