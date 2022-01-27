S = input()

dict = {}
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z']

for alphabet in alphabets:
    dict[alphabet] = 0

for char in S:
    dict[char] += 1

for key, value in dict.items():
    print(value, end=' ')
