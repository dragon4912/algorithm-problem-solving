import sys
input = sys.stdin.readline

M, N = map(int, input().split())        #가로 수, 세로 수

A = []
tomato_list = []
visited = [[0] * M for _ in range(N)]       #익혀진 토마토는 며칠째에 익는지를 방문리스트에 기록
for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

    #BFS 시작 시 모든 토마토를 초기 큐에 넣고 시작해야, 안익은 토마토가 처음 방문될때 가장 빨리 방문된 값임을 보장할 수 있다
    for j, el in enumerate(row):
        if el == 1:
            tomato_list.append([i,j,0])     #세번째 인자는 토마토가 익은 날짜
            visited[i][j] = -1  #방문 리스트에서 익은 토마토는 -1 처리

def is_range(y, x):
    if 0<=y<N and 0<=x<M:
        return True
    return False

from collections import deque
dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def BFS(tomato_list):
    q = deque(tomato_list)  #마지막 인자는 토마토가 익는 경과 일 수
    while q:
        ny, nx, day = q.pop()

        for dy, dx in zip(dys, dxs):
            next_y = ny+dy
            next_x = nx+dx

            if not is_range(next_y, next_x):
                continue
            if visited[next_y][next_x] > 0:
                continue
            if A[next_y][next_x] == 0:
                visited[next_y][next_x] = day+1
                q.appendleft([next_y, next_x, day+1])

BFS(tomato_list)

answer = 0
for i in range(N):
    for j in range(M):
        if A[i][j] == 0:    #안익은 토마토의 위치면서
            if visited[i][j] > 0:  #방문된 곳의 최대 값 찾음
                tmp_answer = visited[i][j]
                answer = max(answer, tmp_answer)
            elif visited[i][j] == 0:    #하나라도 안익은 토마토가 있다면 -1 출력
                answer = -1
                break
    if answer == -1:
        break
print(answer)