import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())     #마을수(=학생수), 도로수, 도착지

A = [[] for _ in range(N+1)]    #0번 인덱스 미사용
for _ in range(M):
    s, e, w = map(int, input().split())
    A[s].append((e,w))

from queue import PriorityQueue
def dijkstra(v):
    D = [10**6] * (N+1)       #거리 최대값은 1000x100
    D[v] = 0        #시작마을은 0
    q = PriorityQueue()
    q.put((0, v))
    visited = [False] * (N+1)
    while q.qsize():
        dis, now = q.get()
        if visited[now]:
            continue
        visited[now] = True

        for next, next_dis in A[now]:
            if visited[next]:
                continue
            if D[next] > D[now]+next_dis:
                D[next] = D[now]+next_dis
                q.put((D[next], next))
    return D

answers = [0] * (N+1)
for v in range(1, N+1):
    d = dijkstra(v)
    answers[v] += d[X]
    if v == X:
        for e, dis in enumerate(d[1:], start=1):
            answers[e] += dis
print(max(answers))