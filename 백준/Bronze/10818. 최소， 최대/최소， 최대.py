import sys
input = sys.stdin.readline

N = int(input().strip())

num_list = list(map(int, input().split()))

#두줄 출력인데 한줄로 잘못 출력함
#채점엔 상관 없었지만 다시 제출
print(min(num_list), max(num_list))
