import sys
input = sys.stdin.readline

N, M = map(int, input().split())
MAX_M = 100000      #문제에서 주어진 최대값

from collections import deque
def BFS(v):
    q = deque([(v, 0)])
    visited = [False] * 200000
    visited[v] = True

    min_sec = sys.maxsize
    while q:
        now, sec = q.pop()
        visited[now] = True
        if now == M:
            if min_sec <= sec:
                continue
            else:   #min_sec > sec
                min_sec = sec
        if now > 110000 or now < 0:
            continue
        
        if not visited[now-1]:
            q.appendleft((now-1, sec+1))
        if not visited[now+1]:
            q.appendleft((now+1, sec+1))
        if now < MAX_M-1 and not visited[now*2]:
            q.appendleft((now*2, sec))
    
    return min_sec

answer = BFS(N)
print(answer)
