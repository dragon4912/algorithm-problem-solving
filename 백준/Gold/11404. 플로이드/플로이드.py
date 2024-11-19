import sys
input = sys.stdin.readline

n = int(input().strip())    #도시 개수
m = int(input().strip())    #버스 개수

A = [[sys.maxsize] * (n+1) for _ in range(n+1)]
for _ in range(m):
    s,e,w = map(int, input().split())
    A[s][e] = min(w, A[s][e])

for k in range(1,n+1):
    for s in range(1,n+1):
        for e in range(1,n+1):
            if A[s][k] + A[k][e] < A[s][e]:
                A[s][e] = A[s][k] + A[k][e]

for i in range(1, n+1):
    A[i][i] = 0
for idx, row in enumerate(A[1:], start=1):
    for elem in row[1:]:
        if elem == sys.maxsize:
            elem = 0
        print(elem, end=' ')
    print()