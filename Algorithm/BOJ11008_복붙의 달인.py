"""
split으로 복붙이 가능한 문자열을 제거하고
제거하고 남은 덩어리들의 -1 이 복붙한 횟수
그리고 남은 덩어리들의 길이를 모두 더하면 답이됨
"""
for _ in range(int(input())):
    s, p = input().split()
    rest = s.split(p)
    ans = len(rest)
    for r in rest:
        ans += len(r)
    print(ans - 1)