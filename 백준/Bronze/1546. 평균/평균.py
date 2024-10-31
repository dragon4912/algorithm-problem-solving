import sys
input = sys.stdin.readline

N = int(input().strip())

scores = list(map(int, input().split()))
max_score = max(scores)

answer = sum(scores)/max_score/N*100

print(answer)
