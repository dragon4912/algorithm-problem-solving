import sys
input = sys.stdin.readline
import math

"""
0~1행열은 0~3번 사이로 방문 - 선분 길이 2
2~3행열은 4 ~ 4*4-1 번 사이로 방문 - 선분 길이 4
4~7행열은 4*4 ~ 8*8-1 번 사이로 방문 - 선분 길이 8
8~15행열은 8*8 ~ 16*16-1 번 사이로 방문 - 선분 길이 16
"""

N, r, c = map(int, input().split())


def sol(min_y, min_x, max_y, max_x, min_yx_cell_cnt):

    mid_y = (min_y + max_y+1)//2        #중앙선 바로 아래
    mid_x = (min_x + max_x+1)//2        #중앙선 바로 오른쪽

    if r < mid_y:   #중심선보다 r이 위라면
        y_level = 0
    else:
        y_level = 1
    
    if c < mid_x:   #중심선보다 c가 왼쪽이라면
        x_level = 0
    else:
        x_level = 1
    
    # if mid_y == r and mid_x == c:
    #     return min_yx_cell_cnt + (y_level)*2 + (x_level)
    
    now_group_len = (max_y-min_y+1)
    if now_group_len == 2:
        return min_yx_cell_cnt + (y_level*2 + x_level)

    if y_level == 0:
        max_y = mid_y-1
    else:
        min_y = mid_y
    if x_level == 0:
        max_x = mid_x-1
    else:
        min_x = mid_x
    
    min_yx_cell_cnt += (now_group_len//2)**2 * (2*y_level + x_level)
    
    min_yx_cell_cnt = sol(min_y, min_x, max_y, max_x, min_yx_cell_cnt)
    return min_yx_cell_cnt
    

max_rc = max(r, c)
if max_rc == 0:
    max_len = 2
else:
    max_len = math.ceil(math.log2(max_rc+1))      #찾고자하는 가장 큰 단위의 길이

min_y = min_x = 0
max_y = max_x = 2**(max_len)-1

answer = sol(min_y, min_x, max_y, max_x, 0)
print(answer)