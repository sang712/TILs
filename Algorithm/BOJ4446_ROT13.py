"""
자음과 모음의 경우로 나눠서 같은 딕셔너리 자료 구조에 담았고
입력을 받아 해당 딕셔너리로 인코딩 하는 과정을 통해 답을 출력하였음
"""
vowels = 'a i y e o u'.split() * 2
consonants = 'b k x z n h d c w g p v j q t s r l m f'.split() * 2

eng_to_ROT13 = {}
for idx, vowel in enumerate(vowels):
    eng_to_ROT13[vowel] = vowels[idx + 3]
    eng_to_ROT13[vowel.upper()] = vowels[idx + 3].upper()
    if idx >= 6:
        break

for idx, consonant in enumerate(consonants):
    eng_to_ROT13[consonant] = consonants[idx + 10]
    eng_to_ROT13[consonant.upper()] = consonants[idx + 10].upper()
    if idx >= 20:
        break

while True:
    incode = []
    try:
        sentence = input()
        for str in sentence:
            if str in eng_to_ROT13:
                incode.append(eng_to_ROT13[str])
            else:
                incode.append(str)
        print(''.join(incode))
    except EOFError:
        break