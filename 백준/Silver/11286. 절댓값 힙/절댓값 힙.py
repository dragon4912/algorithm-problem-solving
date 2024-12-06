import sys
input = sys.stdin.readline

N = int(input().strip())

from queue import PriorityQueue
pq = PriorityQueue()

for _ in range(N):
    value = int(input().strip())

    if value == 0:
        if pq.empty():
            print(0)
        else:
            abs_value, real_value = pq.get()
            print(real_value)
    else:
        pq.put((abs(value), value))