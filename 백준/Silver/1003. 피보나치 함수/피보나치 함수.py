import sys
input = sys.stdin.readline

"""
f(0) : 0 한번
f(1) : 1 한번
f(2) : f(0) + f(1) = 0 한 번, 1 한번
f(3) : f(1) + f(2) = 1 한번 + 0한번, 1한번 = 0 한번 + 2 두번
f(4) : f(2) + f(3) = 0한번, 1 한번 + 0한번 + 2 두번

# 점화식 정의
F[n][0] = f(n)이 0을 호출한 횟수
F[n][1] = f(n)이 1을 호출한 횟수

# 점화식
F[n][0] = F[n-1][0] + F[n-2][0]
F[n][1] = F[n-1][1] + F[n-2][1]

# 초기값
F[0][0] = 1 / F[0][1] = 0
F[1][0] = 0 / F[1][1] = 1
"""

T = int(input().strip())

MAX_N = 40      #문제에서 주어진 가장 큰 N

F = [[0, 0] for _ in range(MAX_N+1)]        #0 ~ 41까지 기록
F[0][0] = 1
F[1][1] = 1

for n in range(2, MAX_N+1):
    F[n][0] = F[n-1][0] + F[n-2][0]
    F[n][1] = F[n-1][1] + F[n-2][1]


for _ in range(T):
    n = int(input().strip())
    print(F[n][0],  F[n][1])