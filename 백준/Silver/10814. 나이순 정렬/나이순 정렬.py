import sys
input = sys.stdin.readline

N = int(input().strip())

user_info = []
for uid in range(N):
    old, name = input().split()
    user_info.append([int(old), uid, name])

user_info.sort(key=lambda x: [x[0],x[1]])

for user in user_info:
    print(f"{user[0]} {user[2]}")