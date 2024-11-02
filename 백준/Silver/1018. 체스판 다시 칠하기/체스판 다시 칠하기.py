import sys
input = sys.stdin.readline

N, M = map(int, input().split())

coors = []
for _ in range(N):
    row = input().strip()
    coors.append(row)


def check_chess_board(min_y, min_x):
    paint_white = 0     #좌상단이 흰색인 체스판 만들때 필요한 페인트 횟수
    paint_black = 0
    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:        #좌표 합이 짝수면 흰색(좌상단이 흰색인 경우)
                cell = 'W'
            else:
                cell = 'B'          #좌표 합이 홀수면 검은색(좌상단이 검은색인 경우)

            #현재 탐색하는 보드가 정답과 다르다면 paitn 횟수 1 증가
            if coors[min_y+i][min_x+j] != cell:
                #좌상단이 흰색인 체스판이, 현재 정답 cell과 다르면 카운팅
                paint_white += 1
            else:
                #좌상단이 흰색인 체스판이, 현재 정답 cell과 같다면 -> 이떄는 검은색 시작 체스판이 cell과 다름
                paint_black += 1
    return min(paint_white, paint_black)


answer = 5000   #보드판 최대 크기는 50*50
for y in range(N-7):     #한번에 8개의 row를 탐색해야하므로 min_y는 N-7까지만 가능
    for x in range(M-7):
        paint = check_chess_board(y,x)
        answer = min(answer, paint)
print(answer)