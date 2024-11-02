import sys
input = sys.stdin.readline

N = int(input().strip())

A = {}
for num in map(int, input().split()):
    A[num] = 1

M = int(input().strip())
for num in map(int, input().split()):
    if A.get(num):
        print(1)
    else:
        print(0)
