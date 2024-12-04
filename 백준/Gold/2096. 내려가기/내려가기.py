import sys
input = sys.stdin.readline

N = int(input().strip())


accum_min_value = [0, 0, 0]
accum_max_value = [0, 0, 0]
for _ in range(N):
    values = list(map(int, input().split()))

    #max값 계산
    first_value = max(accum_max_value[0], accum_max_value[1]) + values[0]
    second_value = max(accum_max_value) + values[1]
    third_value = max(accum_max_value[1], accum_max_value[2]) + values[2]
    accum_max_value = [first_value, second_value, third_value]

    #min값 계산
    first_value = min(accum_min_value[0], accum_min_value[1]) + values[0]
    second_value = min(accum_min_value) + values[1]
    third_value = min(accum_min_value[1], accum_min_value[2]) + values[2]
    accum_min_value = [first_value, second_value, third_value]

answer_max = max(accum_max_value)
answer_min = min(accum_min_value)
print(answer_max, answer_min)
