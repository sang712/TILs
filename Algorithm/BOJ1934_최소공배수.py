'''
최소공배수(Least Common Multiple)를 구하는 방법은
두 수를 곱해서
최대공약수(Greatest Common Divisor)로 나누면 됨
math에도 최소 공배수는 함수로 존재하지 않음 ㅠ
gcd는 유클리드 호제법을 통해 구해짐
유클리드 호제법은
두 수 중 큰 수를 작은 수로 나눈 뒤에
1. 나누어 떨어지면 그 수가 최대공약수
2. 나누어 떨어지지 않으면 나머지와 나눈 수로 위의 과정을 재귀적으로 진행함
'''
from math import gcd

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
