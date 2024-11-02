import sys
input = sys.stdin.readline

N = int(input().strip())

coors = []
for _ in range(N):
    x,y = map(int, input().split())
    coors.append([x,y])

for x, y in sorted(coors):
    print(x, y)