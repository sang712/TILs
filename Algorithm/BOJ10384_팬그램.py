"""
딕셔너리 자료구조을 이용해 알파벳을 카운팅하고
카운팅된 값을 이용해 팬그램인지 판단하여 출력하였음
"""
import sys
input = sys.stdin.readline

for n in range(int(input())):
    sentence = input()
    alpha = {}
    for char in sentence:
        if char.isalpha():
            char = char.lower()
            alpha.setdefault(char, 0)
            alpha[char] += 1
    
    pangram = ['Not a pangram', 'Pangram!', 'Double pangram!!', 'Triple pangram!!!']
    num_alpha = 0
    if len(alpha) == 26:
        num_alpha = sorted(alpha.values())[0]
    print(f'Case {n + 1}: {pangram[num_alpha]}')
