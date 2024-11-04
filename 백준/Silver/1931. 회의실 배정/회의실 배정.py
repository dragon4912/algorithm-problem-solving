import sys
input = sys.stdin.readline

N = int(input().strip())

A = []
for _ in range(N):
    s, e = map(int, input().split())
    A.append([s,e])

A.sort(key=lambda x: [x[1], x[0]])


prev_e = -1
answer = 0
for s, e in A:
    if s >= prev_e:
        prev_e = e
        answer += 1
print(answer)
