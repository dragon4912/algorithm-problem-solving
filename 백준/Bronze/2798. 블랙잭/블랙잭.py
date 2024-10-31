import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_list = []
for num in map(int, input().split()):
    if num < M:
        num_list.append(num)
num_list = sorted(num_list)


def solution():
    max_val = 0
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            sum_i_j = num_list[i] + num_list[j]
            if sum_i_j > M:     #i와 j만으로 값을 초과한다면 탐색 종료
                return max_val
            for k in range(j+1, len(num_list)):
                value = sum_i_j + num_list[k]
                if value > M:
                    break
                if value == M:  #M을 찾았으면 탐색 종료
                    return M
                
                max_val = max(max_val, value)

    return max_val

answer = solution()
print(answer)