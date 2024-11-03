import sys
input = sys.stdin.readline
import math

N, M = map(int, input().split())

A = list(map(int, input().split()))
A.sort(reverse=True)
A = A + [0]     #마지막 나무에 땅바닥까지 가기 위한 값 추가


if N==1:
    answer = M

accum_trees = 0         #현재 탐색중인 idx 이전까지 누적된 나무 절단량
for tree in range(1, len(A)):
    prev_tree = tree - 1
    diff = A[prev_tree] - A[tree]

    if accum_trees + (diff*tree) < M:      #현재 나무 직전까지 잘라도 모자란 경우는 더 자름
        accum_trees = accum_trees + (diff * tree)
        continue
    
    needed_trees = M - accum_trees  #필요한 나무량
    # 1미터 내릴때마다 1*tree만큼 절단됨(tree : 나무 id이면서, 1미터 내릴때 절단되는 나무 개수)
    answer = A[prev_tree] - math.ceil(needed_trees / tree)
    break

print(answer)