import sys
input = sys.stdin.readline
N = int(input())
pair = dict()
for _ in range(N):
    mentor, mentee = input().split()
    pair.setdefault(mentor, [])
    pair[mentor].append(mentee)

ans = []
for mentor in sorted(pair.keys()):
    for mentee in sorted(pair[mentor], reverse=True):
        ans.append(' '.join((mentor, mentee)))
print(*ans, sep='\n')