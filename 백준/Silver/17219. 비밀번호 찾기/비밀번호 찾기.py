import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = {}
for _ in range(N):
    site, pwd = input().split()
    A[site] = pwd

for _ in range(M):
    site = input().strip()
    print(A[site])