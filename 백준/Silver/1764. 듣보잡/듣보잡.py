import sys
input = sys.stdin.readline

N, M = map(int, input().split())

bo = {}
for _ in range(N):
    bo_name = input().strip()
    bo[bo_name] = 1

answer = []
for _ in range(M):
    dud_name = input().strip()

    if bo.get(dud_name):
        answer.append(dud_name)

print(len(answer))
answer.sort()
for name in answer:
    print(name)