import sys
input = sys.stdin.readline

while True:
    num = input().strip()
    if num == '0':
        break

    p1 = 0
    p2 = len(num)-1

    answer = 'yes'
    while p1 < p2:
        if num[p1] != num[p2]:
            answer = 'no'
            break
        p1 += 1
        p2 -= 1
    print(answer)