
import sys
input = sys.stdin.readline

K, N = map(int, input().split())    #랜선 개수, 필요한 랜선 개수

lan_cables = []
max_lan_cable = 0
for _ in range(K):
    cable = int(input().strip())
    lan_cables.append(cable)
    if cable > max_lan_cable:
        max_lan_cable = cable

split_cable = max_lan_cable     #가장 긴 케이블 길이로 시작
prev_min_cable = 1
prev_max_cable = max_lan_cable
while prev_min_cable <= prev_max_cable:
    split_cable = (prev_min_cable + prev_max_cable) // 2

    result_cnt = 0
    for cable in lan_cables:
        cnt = cable // split_cable
        result_cnt += cnt
    # print(result_cnt, split_cable, f"[{prev_min_cable},{prev_max_cable}]")

    if result_cnt < N:      #랜선이 길다면(개수 부족) 다음 탐색은 더 짧게
        prev_max_cable = split_cable - 1
    else:                   #랜선이 짧으면(개수 넘침) 다음 탐색은 더 길게
        prev_min_cable = split_cable + 1
    
    if prev_min_cable > prev_max_cable:
        answer = prev_max_cable
        break

print(answer)