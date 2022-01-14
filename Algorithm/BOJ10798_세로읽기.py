def print_letter(word, idx):
    length = len(word)
    if idx < length:
        print(word[idx], end="")
    else:
        return

word1 = input()
word2 = input()
word3 = input()
word4 = input()
word5 = input()

for i in range(15):
    print_letter(word1, i)
    print_letter(word2, i)
    print_letter(word3, i)
    print_letter(word4, i)
    print_letter(word5, i)
