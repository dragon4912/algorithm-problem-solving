import sys
input = sys.stdin.readline


while True:
    a,b,c = map(int, input().split())
    if a==0:
        break

    if a > b and a > c:
        max_line = a
        lines = [b,c]
    elif b > a and b > c:
        max_line = b
        lines = [a,c]
    elif c > a and c > b:
        max_line = c
        lines = [a,b]

    #최대 변 길이가 30000이라 제곱해도 9억임
    max_line = max_line**2
    lines = [line**2 for line in lines]

    if max_line == sum(lines):
        print('right')
    else:
        print('wrong')