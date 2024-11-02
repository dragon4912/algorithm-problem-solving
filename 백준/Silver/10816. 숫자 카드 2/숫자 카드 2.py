import sys
input = sys.stdin.readline

N = int(input().strip())

A = {}
for num in input().split():
    if A.get(num):
        A[num] += 1
    else:
        A[num] = 1

M = int(input().strip())
for num in input().split():
    print(A.get(num, 0), end=' ')