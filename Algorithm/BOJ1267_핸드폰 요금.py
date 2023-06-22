N = int(input())
time_on_the_phone = list(map(int, input().split()))
estimate_30 = estimate_60 = 0
for time in time_on_the_phone:
    div, mod = divmod(time + 1, 30)
    estimate_30 += div * 10 + (mod > 0) * 10
    div, mod = divmod(time + 1, 60)
    estimate_60 += div * 15 + (mod > 0) * 15
if estimate_30 < estimate_60:
    print(f'Y {estimate_30}')
elif estimate_60 < estimate_30:
    print(f'M {estimate_60}')
else:
    print(f'Y M {estimate_60}')