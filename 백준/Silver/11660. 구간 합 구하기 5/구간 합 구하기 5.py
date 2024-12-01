import sys
input = sys.stdin.readline

N, M = map(int, input().split())    #표 크기, 질의 횟수
A = [[0]*(N+1)]     #구현 편의를 위해 0행과 0열은 0으로 채움
D = [[0]*(N+1) for _ in range(N+1)]   #D[i][j] = A[1][1]부터 A[i][j]까지의 합
for _ in range(N):
    A.append([0] + list(map(int, input().split())))


#구간합 계산
for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(answer)