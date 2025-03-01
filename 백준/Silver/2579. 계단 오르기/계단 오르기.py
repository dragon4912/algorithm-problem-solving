import sys
input = sys.stdin.readline

"""
DP[n][interval] : 이전 계단과의 차이가 interval 일 때, n번째 계단부터 얻을 수 있는 최대 점수

# 정의
DP[n][1] = DP[n+2][2] + A[n]       #n-1번 계단과 n번 계단을 밟음 : 무조건 interval=2로 n+2 계단 밟아야함
DP[n][2] = max(DP[n+1][1], DP[n+2][2]) + A[n]       #n-2번 계단과 n번 계단을 밟음 : interval=1 / n+1과 interval=2 / n+2 중 선택해 밟음

#초기값
DP[n][1] : A[n]
DP[n][2] : A[n]
DP[n-1][1] : -inf (n-2와 n-1을 밟았으므로 n을 못밟음)
DP[n-1][2] : A[n-1] + A[n]

시작점에서 1칸 이동으로 시작하는 최대값은 DP[0][2]  #첫 계단에서, 자유롭게 이동(2칸 전으로부터 이동)
시작점에서 2칸 이동으로 시작하는 최대값은 DP[1][2]  #두번째 계단부터 자유롭게 이동(시작에서 2번째 칸으로 점프)
"""

N = int(input().strip())
A = []
for _ in range(N):
    A.append(int(input().strip()))

DP = [[0,0] for _ in range(N)]
DP = [[0,0, 0] for _ in range(N)]   #각 row의 0번 인덱스 미사용

DP[N-1][1] = A[N-1]
DP[N-1][2] = A[N-1]
if N >= 2:
    DP[N-2][1] = -sys.maxsize
    DP[N-2][2] = A[N-2] + A[N-1]

for i in range(N-3, -1, -1):
    DP[i][1] = DP[i+2][2] + A[i]
    DP[i][2] = max(DP[i+1][1], DP[i+2][2]) + A[i]

if N >= 2:
    print(max(DP[0][2], DP[1][2]))
else:
    print(max(DP[0]))
