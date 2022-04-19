S = list(input())
K = input()
numbs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(len(S)-1, -1, -1):
    if S[i] in numbs:
        S.pop(i)
S = ''.join(S)
print(1) if K in S else print(0)