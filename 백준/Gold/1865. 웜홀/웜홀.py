import sys
input = sys.stdin.readline

"""
고려 사항 : 문제에는 시작노드가 주어지지 않는다. 만약 1번 노드에서 시작하면, 음수 사이클을 돌고 1번에 돌아오는 경우가 무조건 있을까?
> 양수 엣지는 항상 양방향이며, 음수 사이클이 양수 엣지와 연결되어 있다면 연결된 모든 양수 엣지는 비용이 더 작아 질 수 있음

1번 노드와 연결되지 않는 음수 사이클이 있는 경우
> 이 경우는 1번노드에서만 시작하면 음수 사이클을 인식하지 못한다
> 따라서 모든 노드에 대해 벨만-포드를 수행하자
>> 단, 한번 수행한 후 이 다음인 sys.maxsize인 노드만(앞선 수행에서 도달하지 못하는 경우) 수행한다
"""

T = int(input().strip())

def solution():
    N, M, W = map(int, input().split())

    A = []  #에지리스트
    for _ in range(M):
        s, e, w = map(int, input().split())
        A.append((s,e,w))
        A.append((e,s,w))
    for _ in range(W):
        s, e, w = map(int, input().split())
        A.append((s, e, -w))
    
    distance = [sys.maxsize] * (N+1)
    def bellman(start): #음수사이클 판별
        distance[start] = 0
        for _ in range(N):      #N-1번 수행
            for s,e,w in A:
                if distance[s] != sys.maxsize and distance[e] > distance[s]+w:
                    distance[e] = distance[s]+w
        #음수 사이클 판별
        for s,e,w in A:
            if distance[s] != sys.maxsize and distance[e] > distance[s]+w:
                return True
        return False
        
    for node in range(1, N+1):
        if distance[node] == sys.maxsize:   #아직 탐색되지 않은 노드
            is_cycle = bellman(node)
            if is_cycle:
                return True
    return False

for _ in range(T):
    is_cycle = solution()
    if is_cycle:
        answer = 'YES'
    else:    
        answer = 'NO'
    print(answer)