"""
요구 사항대로 구현하였음
예시를 보고 대소문자 센서티브 한 것 같아서 따로 처리를 하지 않았음
"""
import sys
input = sys.stdin.readline

en_to_mi = {}
for n in range(int(input())):
    en, _, mi = input().split()
    en_to_mi[en] = mi

for t in range(int(input())):
    k = int(input())
    sentence = input().split()
    for i in range(len(sentence)):
        sentence[i] = en_to_mi[sentence[i]]
    print(' '.join(sentence))
