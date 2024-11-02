
import sys
input = sys.stdin.readline

N = int(input().strip())

vocabs = set()
for _ in range(N):
    vocabs.add(input().strip())
vocabs = list(vocabs)

vocabs.sort(key=lambda x: [len(x), x])

for vocab in vocabs:
    print(vocab)