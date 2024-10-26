"""
최대공약수를 구하는 공식을 이용해 최소공배수를 구하여 답을 도출해냈음
"""

def gcd(a, b):
    if a%b: return gcd(b, a%b)
    return b

N = int(input())
T = list(map(int, input().split()))
t = T[0]
for i in range(1, N-2):
    t = t*T[i] // gcd(t, T[i])
print(t)
