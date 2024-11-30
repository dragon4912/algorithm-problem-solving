import sys
input = sys.stdin.readline

N = int(input().strip())
tree = {}

for _ in range(N):
    node, child1, child2 = input().split()
    tree[node] = []
    for child in (child1, child2):
        tree[node].append(child)

def pre_order(v):
    if v == '.':
        return
    child1, child2 = tree[v]
    
    print(v, end='')
    if child1 != '.':
        pre_order(child1)
    if child2 != '.':
        pre_order(child2)

def in_order(v):
    if v == '.':
        return
    child1, child2 = tree[v]
    
    if child1 != '.':
        in_order(child1)
    print(v, end='')
    if child2 != '.':
        in_order(child2)

def post_order(v):
    if v == '.':
        return
    child1, child2 = tree[v]
    
    if child1 != '.':
        post_order(child1)
    if child2 != '.':
        post_order(child2)
    print(v, end='')

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()