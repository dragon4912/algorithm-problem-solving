import sys
input = sys.stdin.readline


N, K = map(int, input().split())

from collections import deque
def BFS():
    q = deque([[N, 0]])
    visited = [0] * (100001)
    visited[N] = -1

    while q:
        now, sec = q.pop()
        if now == K:
            return sec
        
        for next in [now-1, now+1, 2*now]:
            if next < 0 or next > 100000:
                continue

            flag = False
            if not visited[next]:
                flag = True
            else:
                if visited[next] > sec+1:
                    flag = True
            if flag:
                visited[next] = sec+1
                q.appendleft([next, sec+1])

answer = BFS()
print(answer)