T = int(input())

def solve():
    dp = [0, 0 ,0]
    for i in range(len(stickers[0])):
        d0, d1, d2 = dp
        dp = [max(d1, d2) + stickers[0][i], max(d0, d2) + stickers[1][i], max(d0, d1)]
    return max(dp)

for t in range(T):
    N = int(input())
    stickers = []
    stickers.append(list(map(int, input().split())))
    stickers.append(list(map(int, input().split())))
    print(solve())