import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, list(input().strip()))))

from collections import deque

def is_range(y, x):
    if 0<=y<N and 0<=x<M:
        return True
    return False
dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def BFS(y,x):
    visited = [[False] * M for _ in range(N)]
    visited[y][x] = True
    q = deque([(y,x, 1)]) #3번째 인자는 이동 거리

    while q:
        now_y, now_x, dis = q.popleft()
        if now_y == N-1 and now_x == M-1:
            return dis
        for dy, dx in zip(dys, dxs):
            next_y = now_y + dy
            next_x = now_x + dx
            if not is_range(next_y, next_x) or visited[next_y][next_x] or A[next_y][next_x]==0:
                continue
            visited[next_y][next_x] = True
            q.append((next_y, next_x, dis+1))

answer = BFS(0,0)        #0,0 -> (N-1, M-1 찾기)
print(answer)