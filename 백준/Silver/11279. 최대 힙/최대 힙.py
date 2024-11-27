import sys
input = sys.stdin.readline

N = int(input().strip())
from queue import PriorityQueue
pq = PriorityQueue()
for _ in range(N):
    cmd = int(input().strip())
    if cmd == 0:
        if not pq.empty():
            print(-pq.get())    #음수를 넣었으므로 양수로 바꿔 출력
        else:
            print(0)
    else:
        pq.put(-cmd)    #큰값을 출력해야하므로 음수로 바꿔서 담음