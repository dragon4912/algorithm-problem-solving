import sys
input = sys.stdin.readline

"""
대기 시간의 합이 최소가 되려면 인출이 빠른사람부터 인출을 하면 된다
"""

N = int(input().strip())

A = list(map(int, input().split()))

A.sort()

answer = 0
for idx, time in enumerate(A):
    answer += (N-idx) * time
print(answer)