import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input().strip())

A = [[] for _ in range(N+1)]    #0번 인덱스 미사용
for _ in range(N-1):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

answers = [0] * (N+1)   #각 노드의 부모를 담을 리스트
visited = [False] * (N+1)
def DFS(v):
    
    for next in A[v]:
        if not visited[next]:
            answers[next] = v
            visited[next] = True
            DFS(next)

visited[1] = True
DFS(1)
for answer in answers[2:]:
    print(answer)