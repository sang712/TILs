"""
요행으로 풀 수 있을 줄 알았는데
요행에 포함되지 않는 경우의 수가 많아 경우의 수를 모두 포함시켜주어야 했음
"""
import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-1):
    h1, w1 = stickers[i]
    for j in range(i+1, N):
        h2, w2 = stickers[j]
        if (h1+h2 <= H and max(w1, w2) <= W) or (w1+w2 <= W and max(h1, h2) <= H): 
            ans = max(ans, h1*w1 + h2*w2)
            continue
        elif (w1+h2 <= H and max(h1, w2) <= W) or (h1+w2 <= W and max(w1, h2) <= H): 
            ans = max(ans, h1*w1 + h2*w2)
            continue
        elif (h1+w2 <= H and max(w1, h2) <= W) or (w1+h2 <= W and max(h1, w2) <= H): 
            ans = max(ans, h1*w1 + h2*w2)
            continue
        elif (w1+w2 <= H and max(h1, h2) <= W) or (h1+h2 <= W and max(w1, w2) <= H): 
            ans = max(ans, h1*w1 + h2*w2)
            continue
print(ans)