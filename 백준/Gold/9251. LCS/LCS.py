import sys
input = sys.stdin.readline

"""
구글링 해서 풂

1. 열 번호가 첫번째 문자열의 각 문자고 행 번호가 두번째 문자열의 각 문자인 2차원 DP 테이블 생성
2. 초기화는 str2의 첫문자와 모든 str1의 문자를 비교해 DP[0][j] 업데이트 / str1의 첫문자와 모든 str2를 비교해 DP[i][0] 업데이트
3. DP 테이블 업데이트
    3-1. str[1][:4] = ACA와 str[2][:3] = CA 이고 str1[4] = Y, str2[3] = P인 경우
        j=4, i=3에 대해 두 문자가 다름. ACAY vs CAP는 ACA vs CAP와 ACAY vs CA 중 더 큰 값과 같은 값을 가짐
    3-2. 만약 str1[4] = str2[3] = Q인 경우
        두 문자가 같음. ACAQ vs CAQ는 ACA vs CA에서 공통문자 Q가 추가된것과 같음
        

# 점화식 정의
DP[i][j] : 첫번째 문자열을 j개, 두번째 문자열을 i개 탐색했을때 LCS

# 점화식
if str1[j] == str2[i]:  #두 문자가 같은경우
    DP[i][j] = DP[i-1][j-1]) + 1
else:
    DP[i][j] = max(DP[i-1][j], DP[i][j-1])


"""

A = input().strip()
B = input().strip()
M = len(A)
N = len(B)

DP = [[0] * M for _ in range(N)]

is_common_char = False
for i in range(N):
    if A[0] == B[i]:
        is_common_char = True
    if is_common_char:
        DP[i][0] = 1
is_common_char = False
for j in range(M):
    if A[j] == B[0]:
        is_common_char = True
    if is_common_char:
        DP[0][j] = 1


for i in range(1, N):
    for j in range(1, M):
        ch1 = B[i]
        ch2 = A[j]
        if ch1==ch2:
            DP[i][j] = DP[i-1][j-1] + 1
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1])

def print_DP():
    print('   ' + '  '.join(list(A)))
    for i, dp in enumerate(DP):
        print(B[i], dp)
# print_DP()

answer = DP[N-1][M-1]
print(answer)