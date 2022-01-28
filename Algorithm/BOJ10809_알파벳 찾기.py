S = input()

length = len(S)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

alphabets = {}

for char in alphabet:
    alphabets[char] = -1

for i in range(length):
    char = S[i]
    if alphabets[char] == -1:
        alphabets[char] = i

for char in alphabet:
    print(alphabets[char], end=' ')