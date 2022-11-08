word = input()
if word.startswith(word[::-1]):
    print(1)
else:
    print(0)