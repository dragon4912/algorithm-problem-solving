import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
START = int(input().strip())

A = [[] for _ in range(V+1)]    #0번 인덱스 미사용
for _ in range(E):
    s, e, w = map(int, input().split())
    A[s].append((e,w))


def dijkstra(start):
    q = PriorityQueue()
    q.put((0, start))

    visited = [False] * (V+1)
    D = [sys.maxsize] * (V+1)
    D[start] = 0

    while q.qsize():
        now_w, now = q.get()

        if visited[now]:
            continue
        visited[now] = True

        for next, next_w in A[now]:
            if visited[next]:
                continue
            if D[next] > D[now] + next_w:
                D[next] = D[now] + next_w
                q.put((D[next], next))

    return D

distance = dijkstra(START)
for v, dis in enumerate(distance[1:], start=1):
    if v == START:
        print(0)
    elif dis == sys.maxsize:
        print('INF')
    else:
        print(dis)