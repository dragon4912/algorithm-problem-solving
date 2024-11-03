import sys
input = sys.stdin.readline


V = int(input().strip())
E = int(input().strip())

A = [[] for _ in range(V+1)]    #0번 인덱스 미사용

for _ in range(E):
    s, e = map(int, input().split())

    A[s].append(e)
    A[e].append(s)

from collections import deque
def BFS(v=1):
    q = deque([v])
    visited = [0] * (V+1)
    visited[v] = 1

    warm = 0
    while q:
        now = q.pop()
        #1번 컴퓨터는 감염 컴퓨터 수에 카운트하지 않음

        for next in A[now]:
            if visited[next]:
                continue
            visited[next] = 1
            q.append(next)
            warm += 1       #연결이 있을떄마다 감염 컴퓨터 수 증가
        
        #print(q, visited)
    
    return warm

warm_cnt = BFS(1)
print(warm_cnt)