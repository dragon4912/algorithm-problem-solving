import sys
input = sys.stdin.readline

"""
# 점화식 정의
D[col][row] : if row=0 or1 : col번째 열에서 row번 행의 스티커를 땟을때의, col번째 열까지의 최대 점수 합
            : if row=2 : col번째 열에서 스티커를 때지 않을때의, col번째 열까지의 최대 점수 합

# 점화식
D[n][0] = D[n-1][1] + A[0][n]
D[n][1] = D[n-1][0] + A[1][n]
D[n][2] = max(D[n-1][0], D[n-1][1])

# 초기값
D[0][0] = A[0][0]
D[0][1] = A[1][0]
D[0][2] = 0
"""

T = int(input().strip())

def sol(A, DP):
    """
    A : 입력된 스티커 점수
    DP : 점화식 저장
    """
    DP[0][0] = A[0][0]
    DP[0][1] = A[1][0]

    for col in range(1, len(A[0])):
        DP[col][0] = max(DP[col-1][1], DP[col-1][2]) + A[0][col]
        DP[col][1] = max(DP[col-1][0], DP[col-1][2]) + A[1][col]
        DP[col][2] = max(DP[col-1][0], DP[col-1][1])
    return DP

for _ in range(T):
    N = int(input().strip())
    A = []
    for _ in range(2):
        A.append(list(map(int, input().split())))
    DP = [[0,0,0] for _ in range(len(A[0]))]
    
    DP = sol(A, DP)
    answer = max(DP[N-1])
    print(answer)