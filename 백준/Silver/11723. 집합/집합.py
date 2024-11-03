import sys
input = sys.stdin.readline

M = int(input().strip())

S = set()
def execute(cmd):
    global S
    if cmd == 'all':
        S = set(range(1, 21))
    elif cmd == 'empty':
        S = set()
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            S.discard(x)
        elif cmd == 'check':
            print(1 if x in S else 0)
        elif cmd == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)

for _ in range(M):
    cmd = input().strip()
    execute(cmd)
