import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

from collections import deque

q = deque([[idx] for idx in range(len(A))])

while q:
    lst = q.popleft()

    if len(lst) == M:
        for i in lst:
            print(A[i], end=' ')
        print()
        continue

    for idx in range(len(A)):
        if idx not in lst:
            q.append(lst + [idx])