"""
답은 N! / A! / B! / C! 이므로
큰 수가 나오는 것을 최소화 하기 위해 
이 A, B, C 중 가장 큰 값 +1 부터 N+1까지 1에 곱한 뒤
나머지 두 값을 누적해서 나누어 출력하였음
"""
N, A, B, C = map(int, input().split())

cars = sorted([A, B, C])
ans = 1
for i in range(cars[-1]+1, N+1):
    ans *= i
for j in cars[:-1]:
    for i in range(1, j+1):
        ans //= i
print(ans)