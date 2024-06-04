"""
스테판 쿼리가 이기는 경우만을 따져서 승패의 경우를 나누었고
각 팀이 이기는 경우 하나의 변수로 1, -1로 스위칭하며 저장하였음
만약 비기는 경우는 그냥 -1을 곱해서 편하게 계산할 수 있기 때문
"""
N = int(input())
ace = list(map(int, input().split()))
got = list(map(int, input().split()))

winner = None
streak = 0
ans = 1
for i in range(N):
    if ace[i] == got[i]:
        winner *= -1
        streak = 1
        continue
    
    if ace[i] % 3 + 1 == got[i]:
        if winner == -1:
            streak += 1
        else:
            winner = -1
            streak = 1
    else:
        if winner == 1:
            streak += 1
        else:
            winner = 1
            streak = 1
    ans = max(streak, ans)
print(ans)