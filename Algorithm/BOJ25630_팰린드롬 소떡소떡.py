N = int(input())
soddeok = input()

ans = 0
for i in range(N//2):
    if not soddeok[i] == soddeok[-(1+i)]:
        ans += 1
print(ans)