"""
연속되는 알파벳이 2개 이상일 경우 단어로 취급하도록 하였음
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
cross_word = [input().strip() for _ in range(R)]
words = []
across = []
for i in range(R):
    for j in range(C):
        letter = cross_word[i][j]
        if letter == '#':
            if len(across) >= 2:
                words.append(''.join(across))
            across = []
        else:
            across.append(cross_word[i][j])
    if len(across) >= 2:
        words.append(''.join(across))
    across = []

down = []
for j in range(C):
    for i in range(R):
        letter = cross_word[i][j]
        if letter == '#':
            if len(down) >= 2:
                words.append(''.join(down))
            down = []
        else:
            down.append(cross_word[i][j])
    if len(down) >= 2:
        words.append(''.join(down))
    down = []

words.sort()
print(words[0])