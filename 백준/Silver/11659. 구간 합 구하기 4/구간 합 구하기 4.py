import sys
input = sys.stdin.readline

N, M = map(int, input().split())    #숫자 개수, 테케 개수

numbers = list(map(int, input().split()))

A = [0] * (N+1)     #구간합 저장
for idx, num in enumerate(numbers, start=1):
    A[idx] = A[idx-1] + num


for _ in range(M):
    s, e = map(int, input().split())
    print(A[e] - A[s-1])