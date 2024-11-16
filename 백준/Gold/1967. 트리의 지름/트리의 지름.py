import sys
input = sys.stdin.readline

N = int(input().strip())   #노드 개수
A = [[] for _ in range(N+1)]    #0번 인덱스 미사용
for _ in range(1, N):  #노드가 n개면 트리의 간선은 n-1개
    s, e, w = map(int, input().split())
    A[s].append((e,w))
    A[e].append((s,w))

from collections import deque
def BFS(v):
    visited = [False] * (N+1)
    visited[v] = True
    q = deque([(v, 0)]) #두번째 요소는 이동거리(경로 간의 가중치 합)

    max_node = 0        #가장 먼 거리의 노드
    max_distance = 0    #입력된 v부터 가장 먼 거리
    while q:
        now, now_dis = q.popleft()
        if now_dis > max_distance:
            max_distance = now_dis
            max_node = now

        for next, next_w in A[now]:
            if visited[next]:
                continue
            visited[next] = True
            q.append((next, now_dis+next_w))
    
    return max_node, max_distance

#루트에서 지름의 노드중 하나 찾기
max_node, max_distance = BFS(1)

#지름인 노드에서 다른 지름인 노드 찾기
another_max_node, another_distance = BFS(max_node)
print(another_distance)