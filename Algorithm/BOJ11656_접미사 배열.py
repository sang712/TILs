S = input()

ans = sorted([S[i:] for i in range(len(S))])
print(*ans, sep='\n')