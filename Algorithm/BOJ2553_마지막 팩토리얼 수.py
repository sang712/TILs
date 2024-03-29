"""
2만 이하의 5의 승수는 5, 25, 125, 625, 3125, 15625 로 5^6이므로
팩토리얼 곱을 통해 직전 값에서 추가될 수 있는 0의 최대는 6개임
따라서 곱셈 때마다 유효숫자 7개씩만 남기고 없애면 원하는 값을 구할 수 있음
"""
N = int(input())

ans = 1
for i in range(2, N + 1):
    ans *= i
    while ans % 10 == 0:
        ans //= 10
    ans %= 10_000_000
print(ans % 10)