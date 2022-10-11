'''
구현하였음
'''
d1, m1, y1, n = map(int, input().split())
d2, m2, y2 = map(int, input().split())

days = 0
if d2 < d1:
    days += d2 + 30 - d1
    m2 -= 1
    if m2 == 0: 
        m2 = 12
        y2 -= 1
else:
    days += d2 - d1

if m2 < m1:
    days += (m2 + 12 - m1) * 30
    y2 -= 1
else:
    days += (m2 - m1) * 30

days += (y2 - y1) * 360

date = (((n -1) + days) % 7) +1
print(date)