N, K = map(int, input().split())

h = 0
m = 0
s = 0
h1, h2, m1, m2, s1, s2 = 0, 0, 0, 0, 0, 0
cnt = 0
while not(h == N and m == 59 and s == 60):
    # 이 하단 라인과
    if s >= 60:
        m += 1
        s %= 60
        if m >= 60:
            h += 1
            m %= 60
    # 이 하단 라인의 순서를 바꾸면 답이 맞이 않음
    h1 = h // 10
    h2 = h % 10
    m1 = m // 10
    m2 = m % 10
    s1 = s // 10
    s2 = s % 10

    if s2 == K or s1 == K or m2 == K or m1 == K or h2 == K or h1 == K:
        cnt += 1
    s += 1
print(cnt)