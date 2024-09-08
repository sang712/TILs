"""
문제를 맞춘 시각에 따라 페널티가 주어지므로
빠르게 맞출 수 있는 문제를 먼저 푸는 것이
시간 누적을 적게 만드는 방법
"""
problems = []
for _ in range(11):
    problems.append(tuple(map(int, input().split())))
problems.sort(key=lambda x: x[0])
ans = 0
D = 0
for d, v in problems:
    ans += d + D + v*20
    D += d
print(ans)