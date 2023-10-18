E, S, M = map(int, input().split())

s = 0

if E == S == M:
    print(E)
else:
    while True:
        estimate = s * 28 + S
        if estimate % 15 == E % 15 and estimate % 19 == M % 19:
            print(estimate)
            break
        s += 1
