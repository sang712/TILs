import sys
input = sys.stdin.readline

R, C, Q = map(int, input().split())

K = []
# 1) 구현 - 시간초과
# for _ in range(R):
#     K.append(list(map(int, input().split())))

# 2) 1차원 부분합 - 3288ms
# for _ in range(R):
#     k = list(map(int, input().split()))
#     for i in range(1, C):
#         k[i] += k[i-1]
#     K.append(k)

# 3) 2차원 부분합
for i in range(R):
    k = list(map(int, input().split()))
    for j in range(1, C):
        k[j] += k[j-1]
        if i > 0:
            k[j] += K[i-1][j] - K[i-1][j-1]
    K.append(k)

# 1) 구현    
# def brightness(r1, r2, c1, c2):
#     pixels = (r2-r1+1) * (c2-c1+1)
#     bright = 0
#     for r in range(r1-1, r2):
#         bright += sum(K[r][c1-1:c2])
#     return bright//pixels

# 2) 1차원 부분합
# def brightness(r1, r2, c1, c2):
#     pixels = (r2-r1+1) * (c2-c1+1)
#     bright = 0
#     for r in range(r1-1, r2):
#         bright += K[r][c2-1]
#         if c1 > 1: bright -= K[r][c1-2]
#     return bright//pixels

# 3) 2차원 부분합
def brightness(r1, r2, c1, c2):
    pixels = (r2-r1+1) * (c2-c1+1)
    bright = K[r2-1][c2-1]
    if r1 > 1:
        bright -= K[r1-2][c2-1]
    if c1 > 1:
        bright -= K[r2-1][c1-2]
    if r1 > 1 and c1 > 1:
        bright += K[r1-2][c1-2]
    return bright//pixels

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    print(brightness(r1, r2, c1, c2))