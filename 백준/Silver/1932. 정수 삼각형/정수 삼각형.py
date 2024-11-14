import sys
input = sys.stdin.readline

N = int(input().strip())

A = []
for idx in range(N):
    A.append(list(map(int, input().split())))

D = [[] for _ in range(N)]
D[N-1] = A[N-1] #맨 아래층
for floor in range(N-2, -1, -1):      #아래층부터 탐색
    bottom_floor = floor+1  #현재층의 바로 아래층
    
    elems = [0] * (floor+1)  #층 번호+1만큼 원소 존재
    for elem_idx in range(floor+1):     #층 번호+1만큼 원소 존재
        elems[elem_idx] = A[floor][elem_idx] + max(D[bottom_floor][elem_idx], D[bottom_floor][elem_idx+1])
    D[floor] = elems
print(D[0][0])
