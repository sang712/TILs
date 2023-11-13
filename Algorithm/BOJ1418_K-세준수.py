"""
에라토스테네스의 체를 이용해 K 이하의 소수를 판별하고
N부터 2까지 반복문을 돌면서 K 이하의 소수로 나눠떨어지면 반복해서 나눈 뒤
결과가 1이 되면 카운팅 하는 방식으로 진행하였음
"""
N = int(input())
K = int(input())

colander = [0, 0] + [1] * int(K)
primes_under_K = []

for i in range(2, len(colander)):
    if colander[i]:
        if i <= K:
            primes_under_K.append(i)
        for j in range(i, len(colander), i):
            colander[j] = 0

ans = 1
for i in range(N, 1, -1):
    for prime in primes_under_K:
        while i % prime == 0:
            i //= prime
        if i == 1:
            ans += 1
            break
            
print(ans)