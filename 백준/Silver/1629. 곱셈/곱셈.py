import sys
input = sys.stdin.readline

"""
D[n] = A를 2^n번 곱했을때의 나머지

D[0] = A % C
D[n] = (D[n-1] * D[n-1]) % C
"""

A, B, C = map(int, input().split())

import math
max_N = math.floor(math.log2(B))
D = [0] * (max_N+1)
D[0] = A % C
for i in range(1, max_N+1):
    D[i] = (D[i-1] * D[i-1]) % C

pow2_sum = []       #B를 2^n들의 합으로 나탈때 필요한 n 리스트
for p in range(max_N, -1, -1):
    if B >= 2**p:
        pow2_sum.append(p)
        B = B - 2**p
        if B == 0:
            break

answer = 1
for pow2_sum_el in pow2_sum:
    answer = (answer * D[pow2_sum_el]) % C
print(answer)