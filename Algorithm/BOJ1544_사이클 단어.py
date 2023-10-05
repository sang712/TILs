import sys
input = sys.stdin.readline

N = int(input())

possible_words = set()
cnt = 0
for _ in range(N):
    word = input().strip()
    if word in possible_words:
        continue
    for i in range(len(word)):
        possible_words.add(word[i:] + word[:i])
    cnt += 1
print(cnt)