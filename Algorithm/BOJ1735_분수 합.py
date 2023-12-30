"""
그냥 분수 합 구하는 공식을 적용하고
유클리드 호제법을 이용해
분수의 합의 최대공약수를 구한 뒤 나눠서 출력 하였음
"""
num1, den1 = map(int, input().split())
num2, den2 = map(int, input().split())

num = num1 * den2 + num2 * den1
den = den1 * den2

def gcd(n1, n2):
    if n1 == n2:
        return n1
    elif n1 > n2:
        bigger, smaller = n1, n2
    else:
        bigger, smaller = n2, n1
    bigger %= smaller
    if bigger == 0:
        bigger = smaller
    return gcd(bigger, smaller)

gcd_ = gcd(num, den)
print(num // gcd_, den // gcd_)