"""
사전에 있는 단어만 의미가 있기 때문에 해당하지 않는 단어가 있으면 0을 출력하면 됨
"""
import sys
input = sys.stdin.readline

dictionary = {}
for n in range(int(input())):
    word = input().strip()
    if len(word) > 2:
        word = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
        dictionary.setdefault(word, 0)
        dictionary[word] += 1
    else:
        dictionary[word] = 1
for m in range(int(input())):
    cnt = 1
    sentence = input().split()
    for word in sentence:
        if len(word) > 2:
            word = word[0] + ''.join(sorted(word[1:-1])) + word[-1]
        if word in dictionary:
            cnt *= dictionary[word]
        else:
            cnt = 0
    print(cnt)