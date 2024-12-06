import sys
input = sys.stdin.readline

N = int(input().strip())

import heapq

q = []
for _ in range(N):
    value = int(input().strip())

    if value == 0:
        if q:
            abs_value, real_value = heapq.heappop(q)
            print(real_value)
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(value), value))