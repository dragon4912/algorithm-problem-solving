import sys
input = sys.stdin.readline

T = int(input().strip())

def sol(N, P):
    for i in range(6, N+1):
        P[i] = P[i-1] + P[i-5]
    
    return P

for _ in range(T):
    N = int(input().strip())
    P = [0] * max((N+1), 6)
    P[1] = P[2] = P[3] = 1
    P[4] = P[5] = 2

    P = sol(N, P)
    print(P[N])