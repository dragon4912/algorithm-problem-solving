import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(range(N))      #사람번호를 1~N대신 0~(N-1)로 배정

del_list = []
remove_num = -1
while len(A) > 0:
    remove_num = (remove_num+M) % len(A)

    del_list.append(A[remove_num]+1) #문제 요구사항에 맞는 사람 번호로 변환
    del A[remove_num]
    remove_num -= 1     #한 자리 비워졌으므로 인덱스 이동


answer = '<'
for num in del_list:
    answer += f"{num}, "
print(answer[:-2], end='>')