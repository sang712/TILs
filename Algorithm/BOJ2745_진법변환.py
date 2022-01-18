N, B = input().split()

B = int(B)

length = len(N)
ans = 0
for i in range(length):
    num = ord(N[length-1-i])
    num -= 55 if num >= 65 else 48
    ans += num * pow(B, i)

print(ans)