import sys
input = sys.stdin.readline

N = int(input().strip())

A = []
for _ in range(N):
    row = list(map(int, input().split()))
    A.append(row)

def check_group(sy, sx, ey, ex):
    start_color = A[sy][sx]
    for i in range(sy, ey+1):
        for j in range(sx, ex+1):
            if A[i][j] != start_color:
                return -1
    
    return start_color

answer = [0, 0]     #화이트 정답, 블루 정답
def split_group(sy, sx, ey, ex):
    check = check_group(sy, sx, ey, ex)
    if check != -1:
        answer[check] += 1
    else:
        my = (sy+ey)//2
        mx = (sx+ex)//2

        new_groups = [[sy, sx, my, mx],     #좌상단
                      [sy, mx+1, my, ex],     #우상단
                      [my+1, sx, ey, mx],     #좌하단
                      [my+1, mx+1, ey, ex],     #우하단
                      ]
        for new_group in new_groups:
            split_group(*new_group)

split_group(0, 0, N-1, N-1)
print(answer[0])
print(answer[1])