import sys
input = sys.stdin.readline

N, M = map(int, input().split())        #노드, 엣지

A = [set() for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    A[s].add(e)
    A[e].add(s)

from queue import PriorityQueue
def dijkstra(v):
    visited = [False] * (N+1)
    pq = PriorityQueue()
    pq.put([0, v])      #첫번째 인자는 다른 노드까지 거리
    visited[v] = True
    D = [sys.maxsize] * (N+1)
    D[v] = 0

    while pq.qsize():
        dis, now = pq.get()
        visited[now] = True

        for next in A[now]:
            if not visited[next]:
                if D[next] > dis + 1:
                    D[next] = dis + 1
                    pq.put([dis+1, next])
    return D

min_val = sys.maxsize
min_node = -1
for node in range(1, N+1):
    kb_scores = dijkstra(node)
    kb_result = sum(kb_scores[1:])

    if min_val > kb_result:
        min_val = kb_result
        min_node = node
print(min_node)
