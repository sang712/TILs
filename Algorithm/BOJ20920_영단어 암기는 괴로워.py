"""
딕셔너리 구조로 K보다 긴 단어만 카운팅을 하고
주어진 조건 대로
등장순서가 많은 순, 길이가 긴 순, 사전 순으로 정렬하여 출력하였음
"""
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
counter = {}
for _ in range(N):
    word = input().strip()
    if len(word) >= K:
        counter.setdefault(word, 0)
        counter[word] += 1
print(*sorted(counter.keys(), key=lambda x: (-counter[x], -len(x), x)), sep='\n')
