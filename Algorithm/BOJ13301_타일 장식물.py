"""
피보나치 수를 구하면서 새로 추가되는 타일의 둘레를 더하는 데
기존의 타일과 새로운 타일의 인접한 면은 둘레에서 제외되므로
새로운 타일의 둘레의 1/2을 더해주었음
"""
N = int(input())
fibo = [0, 1]
s = 4
for _ in range(1, N):
    n_fibo = fibo[-1] + fibo[-2]
    fibo.append(n_fibo)
    s += n_fibo * 2
print(s)