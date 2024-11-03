import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())

    A[s].append(e)
    A[e].append(s)


visited = [0] * (N+1)
def BFS(v):

    q = deque([v])
    visited[v] = True

    while q:
        now = q.popleft()
        
        for next in A[now]:
            if visited[next]:
                continue
            visited[next] = True
            q.append(next)

answer = 0
for v in range(1, N+1):
    if not visited[v]:
        BFS(v)
        answer += 1
print(answer)