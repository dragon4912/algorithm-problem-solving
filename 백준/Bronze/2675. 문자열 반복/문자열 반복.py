import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    R, s = input().split()
    R = int(R)

    for c in s:
        for _ in range(R):
            print(c, end='')
    print()