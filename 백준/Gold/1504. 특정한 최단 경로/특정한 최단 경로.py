import sys
input = sys.stdin.readline
from queue import PriorityQueue

"""
강제로 지나야할 노드가 2개밖에 안되므로 다익스트라를 여러번 활용

첫번째 케이스
    1. start -> v1 
    2. v1 -> v2
    3. v2 -> end

두번째 케이스
    1. start -> v2
    2. v2 -> v1
    3. v1 -> end

양방향 그래프이므로 v1에서 시작하는 경로를 뒤집으면 v1에 도착하는 경로가 됨
이를 이용해 v1 시작과 v2 시작만 구함

"""

N, E = map(int, input().split())    #정점, 간선

A = [[] for _ in range(N+1)]    #0번 인덱스 미사용
for _ in range(E):
    s,e,w = map(int, input().split())
    A[s].append((e,w))
    A[e].append((s,w))

start = 1       #1번 노드에서 출발
end = N         #반드시 N번 노드에 도착
v1, v2 = map(int, input().split())  #반드시 지나야 할 2개의 노드


def dijkstra(s):
    q = PriorityQueue()
    q.put((0, s))
    visited = [False] * (N+1)
    D = [sys.maxsize] * (N+1)
    D[s] = 0

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

def check_routes():
    start_v1_dis = dijkstra(v1)     # v1에서 시작하는 최단경로
    start_v2_dis = dijkstra(v2)     # v2에서 시작하는 최단경로
    route1 = start_v1_dis[start] + start_v1_dis[v2] + start_v2_dis[end]   # start -> v1 -> v2 -> end
    route2 = start_v2_dis[start] + start_v2_dis[v1] + start_v1_dis[end]   # start -> v2 -> v1 -> end
    return min(route1, route2)

answer = check_routes()
if answer >= sys.maxsize:
    answer = -1
print(answer)