import sys
input = sys.stdin.readline

eq_str = input().strip()

eq_plus_list = eq_str.split('-')
answer = 0
for idx, eq_elems in enumerate(eq_plus_list):
    eq_sum = sum(map(int, eq_elems.split('+')))
    if idx == 0:
        answer += eq_sum
    else:
        answer -= eq_sum
print(answer)