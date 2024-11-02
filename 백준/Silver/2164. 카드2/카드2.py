import sys
input = sys.stdin.readline

N = int(input().strip())

from collections import deque
q = deque(range(1, N+1))

while len(q) > 1:
    q.popleft()

    q.append(q.popleft())
print(q.pop())
