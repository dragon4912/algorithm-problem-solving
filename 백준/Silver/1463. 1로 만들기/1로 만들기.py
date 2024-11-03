import sys
input = sys.stdin.readline

"""
X가 3으로 나누어 떨어지면, 3으로 나눈다.
X가 2로 나누어 떨어지면, 2로 나눈다.
1을 뺀다.


DP[1] = 0
DP[2] = 1 (1빼기 or 1나누기)
DP[3] = 1 (3나누기)
DP[4] = 1 + DP[2] = 2로 나누면 n=2
DP[5] = 1 + DP[4] = 1 빼면 n=4
DP[6] = 1 + DP[3] or 1 + DP[2] = 2로 나누면 n=3만들기 or 3으로 나누면 n=2

#점화식
현재 숫자에서 1을 빼거나 2로 나누거나 3으로 나누어본다
3가지 경우로 인해 도출되는 op(n)을 DP테이블에서 비교하여 가작 작은 값을 선택하고 1을 더한다
"""

N = int(input().strip())

MAX_N = int(1e6)
DP = [0] * (MAX_N+1)    #0번 인덱스 미사용
DP[1] = 0
DP[2] = 1
DP[3] = 1

for n in range(4, N+1):
    tmp_answer = float('inf')
    if n % 2 == 0:
        tmp_answer = min(tmp_answer, 1 + DP[n//2])
    if n % 3 == 0:
        tmp_answer = min(tmp_answer, 1 + DP[n//3])
    tmp_answer = min(tmp_answer, 1 + DP[n-1])
    
    DP[n] = tmp_answer

print(DP[N])
