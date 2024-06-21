"""
다 풀고 큰 수 연산이라는 카테고리인 것을 알았지만 
파이썬이라 그냥 피보나치 수를 구현하였음
"""
fibo = [0, 1, 1]

n = int(input())
for i in range(2, n):
    fibo.append(fibo[-1] + fibo[-2])
print(fibo[n])