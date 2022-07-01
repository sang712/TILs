N = int(input())

dp = []
for i in range(N):
    R, G, B = map(int, input().split())
    if i == 0:
        dp.append([R, G, B])
    else:
        pre_R, pre_G, pre_B = dp[i-1]
        R = R + min(pre_G, pre_B)
        G = G + min(pre_R, pre_B)
        B = B + min(pre_R, pre_G)
        dp.append([R, G, B])

print(min(dp[N-1]))