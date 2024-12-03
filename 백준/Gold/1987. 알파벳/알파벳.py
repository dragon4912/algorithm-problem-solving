import sys
input = sys.stdin.readline

R, C = map(int, input().split())

A = [[0] * (C+1)]
for _ in range(R):
    row = [0] + list(map(lambda x: ord(x)-65, input().strip()))       #A=0,... Z=25로 치환하여 저장
    A.append(row)

def is_range(y,x):
    if 1<=y<=R and 1<=x<=C:
        return True
    return False

visited_alphabet = [0] * 26
visited = [[False] * (C+1) for _ in range(R+1)]
max_distance = -1
dys = [1,-1,0,0]
dxs = [0,0,1,-1]
def DFS(y, x, distance=0):
    global max_distance
    if distance > max_distance:
        max_distance = distance
    # print(distance, '\t'*distance, y,x,)

    for d in range(4):
        dy, dx = dys[d], dxs[d]
        ny, nx = y+dy, x+dx

        if is_range(ny,nx) and not visited[ny][nx]:
            if visited_alphabet[A[ny][nx]] == 0:        #아직 방문되지 않은 알파벳
                visited[ny][nx] = True
                visited_alphabet[A[ny][nx]] += 1
                DFS(ny, nx, distance+1)
                visited[ny][nx] = False
                visited_alphabet[A[ny][nx]] -= 1

visited[1][1] = True
visited_alphabet[A[1][1]] = 1
DFS(1,1,1)
print(max_distance)