import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

visited = [False] * N
def DFS(elem_list):
    if len(elem_list) == M:
        print(*[A[elem] for elem in elem_list])
        return
    
    last_insert_value = -1
    for next_idx in range(0, N):
        if A[next_idx] == last_insert_value:       #마지막으로 삽입했던 요소와 새로 삽입할 요소의 값이 같으면 패스
            continue
        if visited[next_idx]:   #이미 있는 요소면 패스
            continue
        last_insert_value = A[next_idx]
        visited[next_idx] = True
        DFS(elem_list+[next_idx])
        visited[next_idx] = False

DFS([])