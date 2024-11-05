import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = []
start_y = start_x= 0
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)
    for j, val in enumerate(row):
        if val == 2:
            start_y, start_x = (i,j)

def is_range(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

from collections import deque
dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def BFS(y, x):
    q = deque([[y,x, 0]])
    visited = [[-1] * M for _ in range(N)]      #-1이면 미방문상태
    visited[y][x] = 0

    while q:
        ny, nx, step = q.pop()

        for dy, dx in zip(dys,dxs):
            next_y = ny+dy
            next_x = nx+dx

            if not is_range(next_y, next_x) or not visited[next_y][next_x]==-1:
                continue
            if A[next_y][next_x] == 0:
                visited[next_y][next_x] = 0
                continue

            visited[next_y][next_x] = step+1
            q.appendleft([next_y, next_x, step+1])
    return visited

answer = BFS(start_y, start_x)

for i, row in enumerate(answer):
    for j, el in enumerate(row):
        if A[i][j] == 0 and answer[i][j] == -1:
            el = 0
        print(el, end=' ')
    print()
