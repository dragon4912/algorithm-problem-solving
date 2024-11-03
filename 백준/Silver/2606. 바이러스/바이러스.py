import sys
input = sys.stdin.readline


V = int(input().strip())
E = int(input().strip())

A = [[] for _ in range(V+1)]    #0번 인덱스 미사용

for _ in range(E):
    s, e = map(int, input().split())

    A[s].append(e)
    A[e].append(s)

warm = 0
visited = [0] * (V+1)
def DFS(v):
    global warm
    
    for next in A[v]:
        if visited[next]:
            continue
        visited[next] = True
        DFS(next)
        warm += 1

visited[1] = True
DFS(1)
print(warm)