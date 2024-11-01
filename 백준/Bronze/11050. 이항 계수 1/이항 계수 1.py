import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    A[i][0] = 1     #nC0 = 1
    A[i][1] = i     #nC1 = n
    A[i][i] = 1     #nCn = 1

for i in range(2, n+1):
    for j in range(2, i+1):
        A[i][j] = A[i-1][j] + A[i-1][j-1]

print(A[n][m])