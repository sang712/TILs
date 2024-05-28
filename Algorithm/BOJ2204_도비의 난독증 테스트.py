"""
정렬을 할 때 소문자로 변환한 값을 이용해 정렬을 하도록 하여 풀었음
"""
import sys
input = sys.stdin.readline

ans = []
while True:
    N = int(input())
    if not N:
        break
    words = [input().strip() for _ in range(N)]
    words.sort(key=lambda x: x.lower())
    ans.append(words[0])
print(*ans, sep='\n')