import sys
input = sys.stdin.readline

N = int(input().strip())

fruit_list = list(map(int, input().split()))

p_fruit_group_start = 0     #과일 그룹 시작 포인터
p_fruit_group_end = 0       #과일 그룹 마지막 포인터
second_fruit_idx = 0        #두 과일로 이루어진 그룹 중, 마지막 과일의 번호가 시작된 위치
                            #ex) 현재 탐색 그룹이 1 2 2 1 1 1 이면, 마지막으로 1로만 이루어진 그룹이 시작한 위치인 4

answer = 1
for i in range(1, N):       #모두 0으로 초기화 했고, elif문의 idx-1 때문에 0은 제외
    
    if fruit_list[i] == fruit_list[second_fruit_idx]:       #마지막 과일과 현재 과일이 같으면
        p_fruit_group_end = i
    elif fruit_list[i] == fruit_list[second_fruit_idx-1]:      #두 과일중 마지막 과일이 아닌 과일이면
        second_fruit_idx = i
        p_fruit_group_end = i
    else:   #새로운 과일이 나왔으면
        p_fruit_group_start = second_fruit_idx
        second_fruit_idx = i
        p_fruit_group_end = i
    
    # print(f"{i} - 그룹 범위:{p_fruit_group_start}~{p_fruit_group_end} / 마지막 그룹 시작: {second_fruit_idx}")
    answer = max(answer, p_fruit_group_end-p_fruit_group_start+1)
print(answer)
