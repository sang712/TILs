"""
주어진 조건이 크지 않아 바로 카운팅해서 출력하였음
"""
n, d = map(int, input().split())
ans = 0
for i in range(1, n+1):
    ans += str(i).count(str(d))
print(ans)
