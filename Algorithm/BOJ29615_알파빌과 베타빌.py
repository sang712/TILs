"""
대기자 명단 중에서 친구의 수보다 1많은 지점부터 확인하면서
친구에 해당하는 인원 수를 세어 출력하였음
"""
N, M = map(int, input().split())
waiting_list = list(map(int, input().split()))
friends = set(map(int, input().split()))
ans = 0
for p in waiting_list[M:]:
    if p in friends:
        ans += 1
print(ans)
