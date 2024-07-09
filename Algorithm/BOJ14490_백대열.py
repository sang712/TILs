"""
최대 공약수를 구해 나누어서 답을 출력하였음
"""
def gcd(a, b):
    if a % b: return gcd(b, a%b)
    else: return b

n, m = map(int, input().split(':'))
_gcd = gcd(n, m)
print(n//_gcd, m//_gcd, sep=':')
