import sys
input = sys.stdin.readline

N, M = map(int, input().split())    #사람 수, 파티 수
Ks = list(map(int, input().split()))
K = []
if Ks[0] == 0:
    print(M)
    sys.exit()
else:
    K = Ks[1:]

parents = list(range(N+1))  #각 노드의 대표노드. 0번 인덱스 미사용
def find(v):
    if parents[v] == v:
        return v
    else:
        parent = find(parents[v])
        parents[v] = parent
        return parent

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if p1 <= p2:        #둘 중 작은 번호로 묶음
        parents[p2] = parents[p1]
    else:
        parents[p1] = parents[p2]
    return min(p1, p2)


party_group = []
for _ in range(M):
    participants = list(map(int, input().split()))
    if len(participants) <= 1:
        continue
    else:
        first_node = participants[1]
        party_group.append(first_node)  #각 파티별 대표 노드 기록
    
    for participant in participants[2:]:
        union(first_node, participant)

[union(K[0], k) for k in K]    #진실을 아는 사람을 하나의 그룹으로 묶음
known_true_group = find(K[0])
answer = M
for group in party_group:
    if find(group) == known_true_group:
        answer -= 1
print(answer)