import sys
input = sys.stdin.readline

"""
DP[i] : i번쨰 숫자를 위한 최소 제곱합 횟수

DP[i] : 1 ~ sqrt(i)의 제곱을 i에서 뺀 수를 j라 하자
    - DP[j]들 중 최소값을 구하고 1을 더함
        - 48의 경우, 6^2, 5^2, 4^2, 2^1, 1^1 을 빼서 { DP[12], DP[23], DP[32], DP[44], DP[45] } 중 최소값에 1을 더햄
    - DP[j] 자체가 제곱수라면 : 1로 배정


"""

N = int(input().strip())

import math
def get_max_sqrt_nt(n):
    """
    제곱했을때 n보다 작은 어떤 숫자들 중, 최대값 반환
    """
    return int(math.sqrt(n))

DP = [sys.maxsize] * (N+1)

DP[0] = 0       #어떤 숫자가 한 자연수의 제곱이면 DP[0]을 탐색하므로 0으로 배정
DP[1] = 1

for i in range(2, N+1):
    max_sqrt_i = get_max_sqrt_nt(i)

    for j in range(1, max_sqrt_i+1):
        bottom_num = i - j**2
        # print(i, max_sqrt_i, j, bottom_num)
        DP[i] = min(DP[bottom_num]+1, DP[i])

print(DP[N])