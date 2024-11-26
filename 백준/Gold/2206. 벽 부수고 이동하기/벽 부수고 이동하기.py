import sys
input = sys.stdin.readline

"""
구글링 해서 풂

벽을 어디서 부수더라도 벽 부숨에 대한 2차원 방문리스트는 하나만 있으면 됨
1. 먼저 벽을 부쉈지만 오답인 루트
    오답이면 다른 벽을 만났거나 vs 다른 벽을 부순 루트가 BFS로 더 빨리 도달한 경우임
    첫번째 경우는, 오답과 다른 어떤 벽을 부순 루트는 오답이 막힌 벽에 막혀 오답 루트는 방문하지 않음
                만약 벽을 부수지 않고 오답이 막힌 벽을 만나 부수더라도, 이 루트는 정답으로 가지 못하므로 배제되어도 됨
    두번째 경우는 다른 벽을 부순 루트가 먼저 정답 루트에 진입함
        만약 처음 벽을 부순 루트가 정답 루트에 진입하더라도, 다른 벽을 부순 루트가 더 빠르므로 배제되어도 됨
"""

N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, list(input().strip()))))

visited = [[[0,0] for _ in range(M)] for _ in range(N)]     #v[i][j][0]는 벽 안부순 경우, v[i][j][1]은 벽 부순 경우

def is_range(y,x):
    if 0<=y<N and 0<=x<M:
        return True
    return False

from collections import deque
dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def BFS(start_y,start_x):
    q = deque([(start_y,start_x, 1, 0)])   #세번쨰 요소는 이동 횟수, 마지막 요소는 벽 부숨 여부
    visited[start_y][start_x][0] = True
    visited[start_y][start_x][1] = True

    while q:
        now_y, now_x, depth, is_breaked = q.pop()
        if now_y == N-1 and now_x == M-1:
            return depth

        for d in range(4):
            dy,dx = dys[d], dxs[d]
            ny,nx = now_y+dy, now_x+dx

            if not is_range(ny, nx):
                continue
            if A[ny][nx] == 1 and not is_breaked:
                if visited[ny][nx][1]:
                    continue
                visited[ny][nx][1] = True
                q.appendleft([ny,nx,depth+1,1])
            elif A[ny][nx] == 0:
                if visited[ny][nx][is_breaked]:      
                    continue
                if not is_breaked:      #벽을 아직 안부순 상태여도 벽 부숨 방문리스트 체크
                    visited[ny][nx][1] = True
                visited[ny][nx][is_breaked] = True
                q.appendleft([ny,nx,depth+1,is_breaked])
    return -1

answer = BFS(0,0)
print(answer)