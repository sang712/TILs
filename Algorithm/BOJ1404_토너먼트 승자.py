"""
우선 승률을 인접리스트 모양대로 8*8 리스트에 저장하였고
함수를 하나 구현해 각 라운드 별로 이길 확률을 구할 수 있도록 하였음
그리고 결과에서 10^15 로 나눠 원래의 확률 값을 구하면서 소수로써 생기는 오차를 줄이도록 하였음
"""
rates = [[0]*8 for _ in range(8)]

i, j = 0, 1
for num in map(int, input().split()):
    rates[i][j] = num
    rates[j][i] = 100 - num
    j += 1
    if j > 7:
        i += 1
        j = i + 1

def win(a, round):
    if round == 1:
        div, mod = a // 2, (a + 1) % 2
        b = 2*div + mod
        return rates[a][b]
    if round == 2:
        div1, div2 = a // 4, (a // 2 + 1) % 2
        c, d = 4*div1 + 2*div2, 4*div1 + 2*div2 + 1
        return win(a, 1)*(win(c, 1) * rates[a][c] + win(d, 1) * rates[a][d])
    if round == 3:
        div = (a // 4 + 1) % 2
        e, f, g, h = 4*div, 4*div+1, 4*div+2, 4*div+3
        return win(a, 2)*(win(e, 2)*rates[a][e] + win(f, 2)*rates[a][f] +
                          win(g, 2)*rates[a][g] + win(h, 2)*rates[a][h])
ans = [win(i, 3)/100_000_000_000_000 for i in range(8)]
print(*ans)