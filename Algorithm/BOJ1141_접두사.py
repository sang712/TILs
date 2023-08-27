"""
입력된 단어들을 길이 순서대로 정렬한 뒤에 2중 for문을 돌면서
우선이 되는 단어가 이후에 등장하는 단어에 시작부분에 등장하는지 확인하여
조건이 맞다면 N에서 1씩 빼는 방식으로 정답을 도출하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
prefixes = [input().strip() for _ in range(N)]
prefixes.sort(key=lambda prefix: len(prefix))

cnt = N
for i in range(N):
    prefix = prefixes[i]
    for j in range(i + 1, N):
        if prefixes[j].startswith(prefix):
            cnt -= 1
            break
print(cnt)