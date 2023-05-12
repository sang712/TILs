"""
두 문자열이 서로 모음을 바꿔서 다른 하나가 될 수 있는지 확인하는 문제
조건에 맞게 비교를 하였고
같은 문자들로 만들었는지는 dictionary 자료구조를 이용하여 문자의 개수를 카운트하여 비교하였고
모음들만 바꿨는지 여부는 for문을 돌 때 자음일 때만 새로운 리스트에 저장하여
join함수로 합쳐서 비교하였음
"""
N = int(input())

word1 = input()
word2 = input()

vowels = {'a', 'e', 'i', 'o', 'u'}
count_char1 = {}
temp_omit_vowels1 = []
for char in word1:
    count_char1.setdefault(char, 0)
    count_char1[char] += 1
    if not char in vowels:
        temp_omit_vowels1.append(char)
omit_vowels1 = ''.join(temp_omit_vowels1)

count_char2 = {}
temp_omit_vowels2 = []
for char in word2:
    count_char2.setdefault(char, 0)
    count_char2[char] += 1
    if not char in vowels:
        temp_omit_vowels2.append(char)
omit_vowels2 = ''.join(temp_omit_vowels2)

if count_char1 == count_char2 and word1[0] == word2[0] and word1[-1] == word2[-1] and omit_vowels1 == omit_vowels2:
    print('YES')
else:
    print('NO')