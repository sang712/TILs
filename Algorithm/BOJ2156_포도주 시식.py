N = int(input())
dp = [0, 0, 0]
for i in range(N):
    wine = int(input())
    if i == 0:
        dp = [wine, 0, 0]
        continue
    d0, d1, d2 = dp
    dp = [d2 + wine, d0 + wine, max(d0, d1, d2)]
print(max(dp))