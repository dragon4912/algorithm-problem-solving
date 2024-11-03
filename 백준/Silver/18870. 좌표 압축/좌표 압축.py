import sys
input = sys.stdin.readline

N = int(input().strip())

A = list(map(int, input().split()))

sortA = sorted(A)
mapping_A = dict()
mapping_id = 1
for el in sortA:
    if not mapping_A.get(el):
        mapping_A[el] = mapping_id
        mapping_id += 1

for el in A:
    print(mapping_A[el]-1, end=' ')