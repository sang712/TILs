"""
반복문을 통해 fibo를 dp형태로 구현하였음
"""
fibo = [0, 1, 1]
n = int(input())
while len(fibo) <= n:
    fibo.append(fibo[-1] + fibo[-2])
print(fibo[n])