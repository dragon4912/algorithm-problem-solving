import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

def is_range(y,x):
    if 0<=y<N and 0<=x<M:
        return True
    return False

dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def init_map(start_y,start_x, map=None):     #BFS로 공기를 찾고, 치즈가 공기와 맞닿은 테두리 개수를 찾음
    q = deque()
    q.appendleft((start_y, start_x))

    AIR_VALUE = 9
    if not map:
        map = [[0] * M for _ in range(N)]
        map[start_y][start_x] = AIR_VALUE

    cheese_cnt = 0
    while q:
        now_y, now_x = q.pop()
        for d in range(4):
            dy, dx = dys[d], dxs[d]
            ny,nx = now_y+dy, now_x+dx

            if not is_range(ny, nx) or map[ny][nx] == AIR_VALUE:
                continue

            if A[ny][nx] == 1:
                #옆 칸이 치즈면 공기와 닿은 면을 1 추가해줌
                map[ny][nx] += 1
                if map[ny][nx] == 1:    #최초 추가된거면 찾은 치즈 개수 1 증가
                    cheese_cnt += 1

            if A[ny][nx] == 0:
                map[ny][nx] = AIR_VALUE
                q.appendleft((ny,nx))
    
    return map, cheese_cnt

           
#가장자리에는 치즈가 놓이지 않으므로, 0,0 좌표에서 BFS를 돌려 외부 공기를 파악함
#동시에 치즈가 공기와 맞닿은 면을 카운트
air_map, cheese_cnt = init_map(0,0, None)

answer = 0
while cheese_cnt > 0:
    melting_cnt = 0
    for i in range(N):
        for j in range(M):
            if 9>air_map[i][j] >= 2:     #공기랑 맞닿은 면이 2개 이상이면
                A[i][j] = 0       #치즈 녹임
    
    air_map, cheese_cnt = init_map(0, 0, None)

    # print(answer, 'turn ----------------')
    # for m in air_map:
    #     print(m)
    answer += 1

print(answer)
