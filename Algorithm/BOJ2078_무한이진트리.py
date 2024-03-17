"""
좌나 우가 1이 아닌 경우 큰 쪽에서 작은 쪽을 빼는 방식으로 계산하도록 하였는데
이렇게 하는 경우 시간초과가 나게 되어
작은 쪽이 많이 작다면 나눗셈으로 여러번의 반복을 줄일 수 있어 해당 방식으로 수정하였음
이전: python3 시간초과, pypy3 1512ms -> 이후 python3 44ms

+) 추가로 좌나 우가 1인 경우도 나눗셈으로 해결이 가능하긴 하지만 나눈 몫 -1 이라 예외라 따로 처리하였음
"""
L, R = map(int, input().split())

l, r = 0, 0
while L > 1 or R > 1:
    if L == 1:
        r += R - 1
        break
    elif R == 1:
        l += L - 1
        break
    elif L > R:
        l += L // R
        L %= R
    else:
        r += R // L
        R %= L
print(l, r)