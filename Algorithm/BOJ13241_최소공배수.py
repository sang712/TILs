"""
최대공약수를 먼저 구하고
두 수의 곱에서 최대공약수를 나누면
최소공배수(Least common multiplier)를 얻을 수 있음
"""
def gcd(a, b):
    if a % b:
        return gcd(b, a%b)
    return b

def lcm(a, b):
    _gcd = gcd(a, b)
    return a * b // _gcd
A, B = map(int,input().split())

print(lcm(A, B))