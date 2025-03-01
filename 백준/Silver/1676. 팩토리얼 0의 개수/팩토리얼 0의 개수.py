import sys
input = sys.stdin.readline

N = int(input().strip())

num_of_5 = 0        #소인수 분해 시 5 개수

only_5_numbers = []
for i in range(1, N+1):
    if i % 125 == 0:
        num_of_5 += 3
    elif i % 25 == 0:
        num_of_5 += 2
    elif i % 5 == 0:
        num_of_5 += 1
        
print(num_of_5)