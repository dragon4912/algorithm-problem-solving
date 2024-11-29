import sys
input = sys.stdin.readline

N = int(input().strip())

fruit_list = list(map(int, input().split()))

fruit1 = None
fruit2 = None
max_cnt = 0
fruit1_cnt = 0
fruit2_cnt = 0
fruit2_cnt_after_change = 0
is_continuous = False
for i in range(N):
    if fruit_list[i] == fruit2:     #마지막 과일과 이전 과일이 같음
        is_continuous = True
        fruit2_cnt += 1
        fruit2_cnt_after_change += 1
    elif fruit_list[i] == fruit1:   #마지막 과일과 이전 과일이 다르지만 카운팅 되는 과일임
        is_continuous = False
        fruit1_cnt += 1
    else:
        is_continuous = False
    
    if not is_continuous:   #직전 과일과 현재 과일이 다른 경우
        if fruit_list[i] == fruit1:
            fruit1_cnt, fruit2_cnt = fruit2_cnt, fruit1_cnt
        else:
            fruit1_cnt, fruit2_cnt = fruit2_cnt_after_change, 1
            fruit2_cnt_after_change = 1
        fruit1 = fruit2
        fruit2 = fruit_list[i]
    
    max_cnt = max(max_cnt, fruit1_cnt+fruit2_cnt)
print(max_cnt)