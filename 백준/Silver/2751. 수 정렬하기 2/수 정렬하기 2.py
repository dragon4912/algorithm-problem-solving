
import sys
input = sys.stdin.readline

N = int(input().strip())

numbers = []
for _ in range(N):
    numbers.append(int(input().strip()))

for num in sorted(numbers):
    print(num)