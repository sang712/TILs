"""
몸무게는 0이 될 수 없고, 몸무게의 제곱의 차이도 0이 될 수 없다는 것을 알고 넘어가야함
우선 이전 몸무게는 1, 현재 몸무게는 루트 G의 값을 초기값으로 잡았고
둘의 제곱의 차가 조건을 만족하면 답으로 하고 각각의 경우에 따라
이전 몸무게과 현재 몸무게에 1씩 더해서 다음 루프를 돌도록 하였음
만약 이전과 현재 몸무게의 차이가 1이면서 제곱의 차이가 G보다 큰 경우는 루프를 빠져나오도록 하였음
"""
G = int(input())

ans = []
before, current = 1, int(G ** 0.5)
while True:
    g = current ** 2 - before ** 2
    if g == G:
        ans.append(current)
        before += 1
        current += 1
    elif g > G:
        if current - before <= 1:
            break
        before += 1
    else:
        current += 1

if ans:
    print(*sorted(ans), sep='\n')
else:
    print(-1)