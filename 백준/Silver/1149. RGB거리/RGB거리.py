import sys
input = sys.stdin.readline

"""
D[house][color] : house에서 color를 칠했을때, 이 이후 칠하는데 드는 최소비용

D[N][color] : 마지막 집 color 비용
D[N-1] ...
    D[N-1][0] : min(D[N][1], D[N][2]) + A[N-1][0]
    D[N-1][1] : min(D[N][0], D[N][2]) + A[N-1][1]
    D[N-1][2] : min(D[N][0], D[N][1]) + A[N-1][2]
"""

N = int(input().strip())

A = []
for _ in range(N):
    r,g,b = map(int, input().split())
    A.append([r,b,g])
D = [[0] * 3 for _ in range(N)]
for color in range(3):
    D[N-1][color] = A[N-1][color]

for house in range(N-2, -1, -1):    #N-1(마지막 집)은 이미 채움
    D[house][0] = min(D[house+1][1], D[house+1][2]) + A[house][0]
    D[house][1] = min(D[house+1][0], D[house+1][2]) + A[house][1]
    D[house][2] = min(D[house+1][0], D[house+1][1]) + A[house][2]

print(min(D[0]))