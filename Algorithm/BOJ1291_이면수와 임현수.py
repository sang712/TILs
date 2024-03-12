"""
문제가 너무 길고 모호한 부분이 있다고 판단되는 경우도 있어 풀기에 조금 난감했음
문제의 지문을 정리하자면 다음과 같음
이면수: 5를 초과하는 수 중 각 자리수의 합이 홀수인 수
임현수: 2, 4 또는 합성수 중 소인수의 종류 개수가 짝수 개인 수
성경수: 그 외

이때 1을 예외처리하지 않으면 임현수로 처리되므로 예외를 처리하기
"""
num = int(input())
prime_nums = []
colander = [0] * 2701
colander[0], colander[1] = 1, 1
for i in range(2, 2701):
    if not colander[i]:
        prime_nums.append(i)
        for j in range(i, 2701, i):
            colander[j] = 1

def imyeonsu(num):
    if num > 5:
        cnt = 0
        while num:
            num, mod = divmod(num, 10)
            cnt += mod
        if cnt % 2:
            return True
    return False

def imhyeonsu(num):
    if num == 2 or num == 4:
        return True
    if num in prime_nums:
        return False
    primes = set()
    for prime in prime_nums:
        while num % prime == 0:
            num //= prime
            primes.add(prime)
    if len(primes) % 2:
        return False
    return True
ans = [[3,2],[1,4]]
print(ans[imyeonsu(num)][imhyeonsu(num)] if num > 1 else 3)