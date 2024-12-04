import sys
input = sys.stdin.readline

N = int(input().strip())
A = [[], [], []]        #100000x3은 약 13MB 필요  / 3x100000은 3MB필요
for _ in range(N):
    v1,v2,v3 = list(map(int, input().split()))
    A[0].append(v1)
    A[1].append(v2)
    A[2].append(v3)


accum_min_value = [elem[N-1] for elem in A]
accum_max_value = [elem[N-1] for elem in A]
for i in range(N-2, -1, -1):    #N-2 ~ 0
    #max값 계산
    first_value = max(accum_max_value[0], accum_max_value[1]) + A[0][i]
    second_value = max(accum_max_value) + A[1][i]
    third_value = max(accum_max_value[1], accum_max_value[2]) + A[2][i]
    accum_max_value = [first_value, second_value, third_value]

    #min값 계산
    first_value = min(accum_min_value[0], accum_min_value[1]) + A[0][i]
    second_value = min(accum_min_value) + A[1][i]
    third_value = min(accum_min_value[1], accum_min_value[2]) + A[2][i]
    accum_min_value = [first_value, second_value, third_value]

answer_max = max(accum_max_value)
answer_min = min(accum_min_value)
print(answer_max, answer_min)
