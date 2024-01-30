"""
입력이 크지 않아 브루트포스 알고리즘으로 그냥 하나하나 다 해보는 방식으로 구현하였음
시작 coke 값을 t로 두지 않고 10000으로 두어서 틀린 줄 알았는데 (맞고 나서 다시 10000으로 바꾸니 영향 없었음)
그게 아니라 i가 0일 때를 고려하지 않아서 그런 것이었음
"""
n, m, t = map(int, input().split())

burgers, coke = 0, t
for i in range(t // n + 1):
    j, time_remains = divmod(t - i*n, m)
    if time_remains < coke:
        coke = time_remains
        burgers = i + j
    elif time_remains == coke:
        burgers = max(burgers, i + j)
print(burgers, coke)