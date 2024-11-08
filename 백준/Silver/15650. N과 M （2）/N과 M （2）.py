import sys
input = sys.stdin.readline

""" 4C3 기준
BFS()로 현재보다 큰 숫자를 모두 탐색하며, depth=M이 되면 출력
1 > 2 > 3
      > 4
  > 3 > 4
  > 4 (더 이상의 원소가 없으므로 1을 시작으로 하는 탐색 끝)
2 > 3 > 4
  > 4 (더 이상의 원소가 없으므로 2를 시작으로 하는 탐색 끝)
"""

N, M = map(int, input().split())

from collections import deque

#q = deque([[i] for i in range(1,N+1)])
q = deque([[i] for i in range(1,N+1 - M +1)])      #12C4라면 마지막 값의 원소가 9(=N+1-M)이므로 10부터는 탐색 필요 없음

while q:
    route = q.popleft()
    now = route[-1]     #마지막 삽입되었던 값

    if len(route) == M:
        for el in route:
            print(el, end=' ')
        print()
        continue
    for i in range(now+1, N+1):
        q.append(route + [i])
