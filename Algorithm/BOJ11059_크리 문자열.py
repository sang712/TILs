S = list(map(int, input()))

len_s = len(S)
ans = False
for l in range(len_s-len_s%2, 0, -2):
    for i in range(len_s-l+1):
        if sum(S[i:i+l//2]) == sum(S[i+l//2:i+l]):
            ans = True
            break
    if ans:
        print(l)
        break