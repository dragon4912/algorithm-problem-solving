import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

from collections import deque
def BFS():
    q = deque([[]]) #빈 배열로 시작

    while q:
        elem_list = q.pop()
        if len(elem_list) == M:
            print(*[A[elem] for elem in elem_list])
            continue

        last_insert_value = -1
        for next_idx in range(0, N):
            if A[next_idx] == last_insert_value:       #마지막으로 삽입했던 요소와 새로 삽입할 요소의 값이 같으면 패스
                continue
            if next_idx in elem_list:   #이미 있는 요소면 패스
                continue
            last_insert_value = A[next_idx]
            q.appendleft(elem_list+[next_idx])
BFS()
