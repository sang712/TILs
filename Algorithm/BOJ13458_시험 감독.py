N = int(input())
As = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for testtaker in As:
    testtaker -= B
    ans += 1
    # 7번 라인에서 testtaker가 음수가 되는 경우 ans의 값이 작아지므로 검사가 필요함
    if testtaker > 0:
        ans += testtaker // C
        testtaker %= C
        if testtaker > 0:
            ans += 1

print(ans)