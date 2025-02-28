import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

H, W = map(int, input().split())    #세로, 가로

A = []
for _ in range(H):
    row = input().strip().replace("H", "0")     #구멍을 숫자 0으로 대체
    A.append(list(map(int, list(row))))

def is_range(y, x):
    if 0<=y<H and 0<=x<W:
        return True
    return False


visited = [[False] * W for _ in range(H)]
dys,dxs = [1,-1,0,0], [0,0,1,-1]
D = [[0] * W for _ in range(H)]
def DFS(now_y, now_x, now_cnt):
    # print(now_y, now_x)
    
    d_move = A[now_y][now_x]
    max_move_from_now = 0        #현재 좌표에서 최대 이동 거리
    for d in range(4):
        dy,dx = dys[d]*d_move, dxs[d]*d_move
        next_y = now_y+dy
        next_x = now_x+dx

        if not is_range(next_y, next_x) or A[next_y][next_x]==0:   #좌표계 벗어나거나 구멍이면 종료
            max_move_from_now = max(max_move_from_now, 1)
            # print(f'\t\tnow({now_y},{now_x}) is end at {next_y},{next_x}', max_move_from_now,)
            continue

        if visited[next_y][next_x]:     #방문한 곳을 다시 방문한다면, 계속 같은 루트로 무한번 이동 가능
            max_move_from_now = float('inf')
            return max_move_from_now
        
        if D[next_y][next_x]:
            # print(f'\tnow({now_y},{now_x}) get from {next_y},{next_x}', D[next_y][next_x])
            max_move_from_now = max(D[next_y][next_x]+1, max_move_from_now)
        else:
            visited[next_y][next_x] = True
            max_move_from_now = max(DFS(next_y, next_x, now_cnt+1)+1, max_move_from_now)
            # print(f'now({now_y},{now_x}) get from {next_y},{next_x}', max_move_from_now)
            visited[next_y][next_x] = False
        
        #max_move_from_now = max(max_move_from_now, move_from_now)
    D[now_y][now_x] = max_move_from_now
    return max_move_from_now

visited[0][0] = True
answer = DFS(0, 0, 0)
if answer == float('inf'):
    answer = -1
print(answer)