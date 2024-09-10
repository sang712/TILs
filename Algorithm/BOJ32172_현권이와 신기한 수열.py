"""
for문으로 반복하면서 주어진 조건에 따라 수열의 값을 구하였음
"""
N = int(input())
As = {0,}
a = 0
for i in range(1, N+1):
    ai = a - i
    if ai < 0 or ai in As:
        a += i
    else:
        a -= i
    As.add(a)
print(a)