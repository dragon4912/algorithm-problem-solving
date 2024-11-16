import sys
input = sys.stdin.readline

""" 구글링해서 로직 찾고 구현함
A+B*C의 경우
> A 출력 : A
> +는 스택에 담음 : [+]
> B 출력 : AB
> *는 스택의 마지막인(+)보다 연산 순위가 높으므로 스택에 담음 : [+, *]
> C 출력 : ABC
> 문자열이 끝났으므로 스택을 끝까지 pop : ABC*+

A+B*(C-D)의 경우
> A 출력 : A
> +는 스택에 담음 : [+]
> B 출력 : AB
> *는 스택의 마지막인(+)보다 연산 순위가 높으므로 스택에 담음 : [+, *]
> (는 스택의 마지막인(*)보다 연산 순위가 높으므로 스택에 담음 : [+, *, (]
> C 출력 : ABC
> 스택의 마지막이 괄호이므로 어떤 연산자라도 스택에 담음 : [+, *, (, -]
> D 출력 : ABCD
> )인 경우 (를 만날떄까지 스택에서 pop을 수행 : ABCD- / [+, *]
> 문자열이 끝낫으므로 스택을 끝까지 pop : ABCD-*+

A+B-C의 경우
> A 출력 : A
> +는 스택에 담음 : [+]
> B 출력 : AB
> -는 마지막연산자 +와 연산순위가 같으므로 +를 pop하고, 비었으므로 -는 push : AB+ / [-]
> C 출력 : AB+C
> 문자열 끝 : AB+C-

A+B*C-D의 경우
> A 출력 : A
> +는 스택에 담음 : [+]
> B 출력 : AB
> *는 스택의 마지막인 +보다 연산순위가 높으므로 push : [+, *]
> C 출력 : ABC
> -의 경우
    스택의 마지막인 *보다 연산순위가 낮으므로 *을 pop
    *을 pop하고 남은 마지막인 +도 연산순위가 같으므로 +를 pop
    하고 -는 push() : ABC*+ / [+, -]
> D 출력 : ABC*+D
> 문자열 끝 : ABC*+D-
"""

eq = input().strip()

result = ''
operator_stack = []
def get_last_operator():
    if operator_stack:
        return operator_stack[-1]
    else:
        return None

for elem in list(eq):
    if elem in ('+', '-'):
        if get_last_operator() == '(':
            operator_stack.append(elem)
        else:
            while get_last_operator() and get_last_operator() != '(':
                result += operator_stack.pop()
            operator_stack.append(elem)
    elif elem in ('*', '/'):
        if get_last_operator() == '(':
            operator_stack.append(elem)
        else:
            if get_last_operator() == '*' or get_last_operator() == '/':
                result += operator_stack.pop()
            operator_stack.append(elem)
    elif elem == '(':
        operator_stack.append(elem)
    elif elem == ')':
        while operator_stack:
            if get_last_operator() == '(':
                operator_stack.pop()
                break
            else:
                result += operator_stack.pop()
    else:
        result += elem
    #print(elem, result, operator_stack)

for el in reversed(operator_stack):
    result += el
print(result)