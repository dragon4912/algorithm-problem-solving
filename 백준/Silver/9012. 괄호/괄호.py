import sys
input = sys.stdin.readline

T = int(input().strip())

def sol(ps):
    open_cnt = 0
    for c in ps:
        if c == "(":
            open_cnt += 1
        else:
            open_cnt -= 1

        if open_cnt < 0:
            return False
    
    if open_cnt == 0:
        return True
    else:
        return False

for _ in range(T):
    if sol(input().strip()):
        print("YES")
    else:
        print("NO")