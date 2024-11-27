import sys
input = sys.stdin.readline


"""
구글링 해서 풂

점화식 정의 가이드
    1) 선택지 1 - 물건을 담음
    어떤 물건을 배낭에 넣었다고 가정. 남은 용량과 개수로 새로운 가치합 탐색
    ex) 배낭 용량 10kg이고 1번 물건(2kg)을 넣었다고 가정 -> 남은 8kg에서, 2번물건 ~ N번 물건 중 최대 가치합 탐색

    2) 선택지 2 - 물검을 담지 않음
    배냥 용량이 10kg이고, 1번 물건을 건너 뜀 -> 남은 10kg에서 2번물건 ~N번 물건 중 최대 가치합 탐색


# 점화식 정의
D[n][k] : 1~n번째 물건 중에 각각을 담거나or담지 않은 상태에서의 최대 가치합. 1~n번 물건을 담을 배낭의 무게 용량

# 점화식
if W[n] > k:    #남은 용량보다 n번 물건의 무게가 큰 경우
    D[n][k] = D[n-1][k]     #n-1번 물건까지에 대한 최대합
else:
    #두 값중 최대값 선택
    D[n][k] = D[n-1][k - W[n]] + V[n]       #n번 물건 선택
    D[n][k] = D[n-1][k]                     #n번 물건 미선택



"""

N, K = map(int, input().split())

W = [0] * (N)
V = [0] * (N)
for n in range(N):
    w, v = map(int, input().split())
    W[n] = w
    V[n] = v

D = [[0] * (K+1) for _ in range(N)]     # N x (K+1) 크기, 무게는 0~K까지
for k in range(W[0], K+1):  #첫번째 물건을 담을 수 있는 모든 무게애 대해 물건 담은 가치 삽입
    D[0][k] = V[0]

for n in range(1, N):
    for k in range(K+1):
        if k < W[n]:    #물건을 담을 수 없는 경우
            D[n][k] = D[n-1][k]
        else:  #W[n] 이상의 무게일떄
            D[n][k] = max(D[n-1][k-W[n]]+V[n], D[n-1][k])       #max(물건 담기, 물건 안담기)

# for n, d in enumerate(D):
#     print(n,d)
answer = D[N-1][K]
print(answer)