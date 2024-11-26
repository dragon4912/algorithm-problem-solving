import sys
input = sys.stdin.readline

"""
구글링 해서 풂

# 점화식 정의
D[i] : i번째 숫자까지 탐색했을때의 LIS
    D[i][0] : LIS 값
    D[i][1] : LIS 값을 얻었을때 

# 점화식
D[i] : j= 1 ~ i-1로 D[j]을 탐색하며 A[j] < A[i]이면서 가장 큰 D[j]를 찾음
        D[i]는 이 조건을 만족한 D[j]+1이 됨


"""

N = int(input().strip())
A = list(map(int, input().split()))

D = [1] * N     #각 위치에서 수열이 증가하지 못하면 원소하나가 부분수열이 되므로 1로 초기화

answer = 1
for i in range(1, N):
    max_lis = 0
    for j in range(0, i):
        if A[i] > A[j]:
            max_lis = max(max_lis, D[j])
    D[i] = max_lis + 1
    answer = max(answer, D[i])
print(answer)