import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())
A = input().strip()


start = 0
ioi_cnt = 0
is_ioi = False
answer = 0

prev_ch = ''
for i in range(M):
    if is_ioi:
        if A[i] == 'I':
            ioi_cnt += 1
            if prev_ch == 'O':        #이전이 O, 현재는 I인 경우
                pass
            else:                       #II가 연속인 경우
                is_ioi = True
                ioi_cnt = 1
                start = i
                
            #정답 체크
            if ioi_cnt >= N+1:      #I가 M+1개 이상인지 체크
                answer += 1
        elif A[i] == 'O' and prev_ch == 'O':          #OO가 연속인 경우
            is_ioi = False
            ioi_cnt = 0
    else:
        if A[i] == 'I':
            is_ioi = True
            ioi_cnt = 1
            start = i
    
    # print(f"{i}: {is_ioi}, ioi_cnt:{ioi_cnt}, answer:{answer}")
    # print(f"\t{start} to {i} : ", A[start:i+1])
    
    prev_ch = A[i]
        
print(answer)