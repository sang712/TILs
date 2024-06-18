"""
x, y 의 최소 공약수가 a라는 건 x, y모두 a로 나누어 떨어진다는 것이고
x + y 또한 a로 나누어 떨어진다는 것임
따라서 x + y 가 될 수 있는 최소인 2*a 보다 b가 크고 b가 a로 나누어 떨어지면 조건을 만족함
"""
import sys
input = sys.stdin.readline

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())
    print(1) if 2*a <= b and b%a == 0 else print(0)