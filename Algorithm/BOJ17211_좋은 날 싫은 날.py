"""
좋은날일 때 다음 날이 좋은날일 확률과 나쁜날일 때 다음 날이 좋은날일 확률
좋은날일 때 다음 날이 나쁜날일 확률과 나쁜날일 때 다음 날이 나쁜날일 확률을
N회 반복하여 답을 구하였음
"""
N, feeling = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

ans = [1-feeling, feeling]

for _ in range(N):
    goodday, badday = ans
    ans = [goodday*gg + badday*bg, goodday*gb + badday*bb]

print(f'{ans[0]*1000:.0f}\n{ans[1]*1000:.0f}')