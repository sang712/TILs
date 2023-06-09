"""
세 부분으로 나눌 때 필요한 인덱스는 2개임을 간과하고
3중 for문으로 구현하려고 해서 한 번 틀렸고
3중 for문을 2중 for문으로 구현하면서 range범위를 수정하지 않아서 한 번 더 틀렸음
"""
word = input()
length = len(word)

dictionary = []
for i in range(1, length - 1):
    for j in range(i + 1, length):
        dictionary.append(word[:i][::-1] + word[i:j][::-1] + word[j:][::-1])

print(sorted(dictionary)[0])