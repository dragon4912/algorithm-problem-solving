import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input().strip())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    parent, *nodes = map(int, input().split())
    nodes = nodes[:-1]  #마지막 -1 제외
    for node, w in zip(nodes[::2], nodes[1::2]):
        tree[parent].append((node, w))


max_node = -1
max_distance = 0
visited = [False] * (N+1)
def DFS(v, accum_w):
    global max_node
    global max_distance

    if accum_w > max_distance:
        max_distance = accum_w
        max_node = v
    
    visited[v] = True
    
    for next, w in tree[v]:
        if not visited[next]:
            DFS(next, accum_w+w)

DFS(1,0)
end_node = max_node    #지름이 되는 노드 중 하나

max_node = -1
max_distance = 0
visited = [False] * (N+1)
DFS(end_node, 0)

print(max_distance)