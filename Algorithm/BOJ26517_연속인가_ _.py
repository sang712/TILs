"""
두 조건이 같은 경우에는 Yes와 f(k)를 출력하고
아닐 경우 No를 출력하도록 하였음
"""
k = int(input())
a, b, c, d = map(int, input().split())

if a*k + b == c*k + d:
    print('Yes', a*k + b)
else:
    print('No')