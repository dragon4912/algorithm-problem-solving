import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a,b = min(n,m), max(n,m)

while True:
    share, rest = divmod(b,a)

    if rest == 0:
        gcd = min(a,b)
        break

    a,b = min(rest, a), max(rest,a)

lcm = n*m//gcd
print(gcd)
print(lcm)
    