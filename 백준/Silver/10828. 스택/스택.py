import sys
input = sys.stdin.readline

N = int(input().strip())

A = []
for _ in range(N):
    cmd = input().strip()

    if cmd.startswith('push'):
        num = int(cmd.split()[1])
        A.append(num)
    elif cmd == 'pop':
        print(A.pop() if A else -1)
    elif cmd == 'size':
        print(len(A))
    elif cmd == 'empty':
        print(0 if A else 1)
    elif cmd == 'top':
        print(A[-1] if A else -1)