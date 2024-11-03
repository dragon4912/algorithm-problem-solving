import sys
input = sys.stdin.readline

N = int(input().strip())

from queue import PriorityQueue
pq = PriorityQueue()
for _ in range(N):
    cmd = int(input().strip())
    if cmd == 0:
        if pq.empty():
            print(0)
        else:
            print(pq.get(0))
    else:
        pq.put(cmd)