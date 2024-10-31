import sys
import math

input = sys.stdin.readline

N = int(input().strip())

t_shirt_list = map(int, input().split())
T, P = map(int, input().split())

T_answer = 0
for t_shirt in t_shirt_list:
    T_answer += math.ceil(t_shirt / T)

P_bundle, P_single = divmod(N, P)

print(T_answer)
print(P_bundle, P_single)
