import sys
input = sys.stdin.readline

N = int(input().strip())
DIVIDOR = 10007

D = [0] * (N+1)
D[1] = 1    # |
if N >=2:
    D[2] = 3    # || = ㅁ

for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]*2) % DIVIDOR

print(D[N])