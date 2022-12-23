'''
제한조건 n <= 1_000_000_000_000_000_000 (백 경)

피보나치를 행렬으로 된 거듭제곱으로 나타낼 수 있다는 것을 처음 알게 되었고
블로그들을 보면서 내가 알고 이해한 내용을 정리하면서 문제를 풀었다.
시간이 꽤나 많이 소요되었지만 남는 것이 있으니 괜찮다고 생각한다.
'''
denom = 1_000_000_007
def fibo(n: int) -> int:
    if n in fibo_remainder:
        return fibo_remainder[n]
    
    if n % 2 == 0:
        fm = fibo(n // 2) % denom
        fm_1 = fibo(n // 2 - 1) % denom
        f = ((fm + fm_1) * fm + fm * fm_1) % denom
    else:
        f = (fibo(n // 2 + 1) ** 2 + fibo(n // 2) ** 2) % denom
    fibo_remainder[n] = f
    return f

n = int(input())
fibo_remainder = {0: 0, 1: 1, 2: 1}
print(fibo(n))