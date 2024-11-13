import sys
input = sys.stdin.readline
from queue import PriorityQueue

V, E = map(int, input().split())
START = int(input().strip())

A = [[] for _ in range(V+1)]    #0번 인덱스 미사용
for _ in range(E):
    s, e, w = map(int, input().split())
    A[s].append((e,w))

def dijstra(v):
    distance = [sys.maxsize] * (V+1)
    distance[v] = 0     #시작점의 가중치는 0
    visited = [False] * (V+1)
    q = PriorityQueue()
    q.put((0, v))

    while not q.empty():
        now_w, now = q.get()
        if visited[now]:
            continue
        visited[now] = True

        for next, next_w in A[now]:
            if visited[next]:
                continue
            if distance[now] + next_w < distance[next]:
                distance[next] = distance[now] + next_w
                q.put((distance[next], next))
    return distance

distance = dijstra(START)
for v, dis in enumerate(distance[1:], start=1):
    if v==START:
        print(0)
    elif dis == sys.maxsize:
        print('INF')
    else:
        print(dis)