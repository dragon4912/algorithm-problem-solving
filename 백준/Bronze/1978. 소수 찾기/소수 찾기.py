import sys
input = sys.stdin.readline

N = int(input().strip())

MAX_NUMBER = 1000
search_max_num = int(MAX_NUMBER**.5) + 1

prime_list = list(range(MAX_NUMBER+2))
prime_list[1] = 0
for num in range(2, search_max_num+1):
    if prime_list[num] == 0:  #이미 소수로 판별된 숫자는, 배수들 지우는 작업 패스함
        continue

    #배수 지움
    for prime_applicant in prime_list[num+1:]:
        if prime_applicant % num == 0:
            prime_list[prime_applicant] = 0


answer = 0
for t in map(int, input().split()):
    if prime_list[t]:
        answer += 1

print(answer)
