"""
좌표의 공약수가 있다면 원점과 더 가까운 곳에 시야를 가리는 점이 있다는 뜻이므로
공약수가 1이 나오는 수를 찾아 2를 곱하여 답을 구하였음
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a % b)

C = int(input())
points = [0, 3]
ans = []
for c in range(C):
    N = int(input())
    for i in range(len(points), N+1):
        cnt = 0
        for j in range(1, i):
            if gcd(i, j) == 1:
                cnt += 1
        points.append(points[-1] + cnt*2)
    ans.append(points[N])
print(*ans, sep='\n')