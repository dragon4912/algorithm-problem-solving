import sys
input = sys.stdin.readline

T = int(input().strip())


def is_range(y,x):
    if 0 <= y < N and 0 <= x < M:
        return True
    return False

from collections import deque
def BFS(A, y, x):
    dys = [1,-1,0,0]    #상하좌우
    dxs = [0,0,1,-1]

    q = deque([[y,x]])
    A[y][x] = 2     #방문리스트 대신, 방문은 2로 표현

    while q:
        now_y, now_x = q.popleft()
        for dy, dx in zip(dys, dxs):
            ny = now_y + dy
            nx = now_x + dx

            if not is_range(ny, nx):    #좌표 벗어남
                continue

            if A[ny][nx] == 2:  #이미 방문
                continue
                
            if A[ny][nx] == 1:
                A[ny][nx] = 2
                q.append([ny, nx])

def sol(M, N, K):
    A = [[0] * (M) for _ in range(N)]   #배추 밭 좌표
    for _ in range(K):
        x, y = map(int, input().split())
        A[y][x] = 1
    
    answer = 0
    for y in range(N):
        for x in range(M):
            if A[y][x] == 1:
                BFS(A, y, x)
                answer += 1
    return answer


global M
global N
for _ in range(T):
    M, N, K = map(int, input().split())     #가로길이, 세로길이, 배추 수
    
    answer = sol(M, N, K)
    print(answer)