import sys
input = sys.stdin.readline

""" 두번쨰 풀이
첫번째 풀이때는 각 노드->X까지의 최단거리를 찾기 위해 모든 노드에서 X까지 다익스트라를 구했다
start->end를 뒤집은 인접리스트로 X로 시작해 다익스트라를 구하면 각 노드에서 X로 가는 최단거리가 된다
"""

N, M, X = map(int, input().split())     #마을수(=학생수), 도로수, 도착지

A = [[] for _ in range(N+1)]    #0번 인덱스 미사용
reverse_A  = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    A[s].append((e,w))
    reverse_A[e].append((s,w))

from queue import PriorityQueue
def dijkstra(A, v):
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

forward_distance = dijkstra(reverse_A, X)       #각 노드에서 X까지 거리
backward_distance = dijkstra(A, X)              #X에서 각 노드까지 거리

answer = 0
for v in range(1, N+1):
    answer = max(answer, forward_distance[v] + backward_distance[v])
print(answer)
