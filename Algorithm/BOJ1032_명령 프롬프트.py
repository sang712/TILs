N = int(input())

word = []
for _ in range(N):
    if not _:
        word = list(input())
        continue
    else:
        check = list(input())

    for i in range(len(word)):
        if word[i] == '?' or word[i] == check[i]:
            continue
        else:
            word[i] = '?'

print(''.join(word))