import sys
input = sys.stdin.readline

N = int(input().strip())

#strip 안하면 \n까지 리스트에 저장됨
answer = sum( map(int, list(input().strip())) )
print(answer)