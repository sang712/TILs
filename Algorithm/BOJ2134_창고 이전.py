"""
각 창고의 크기 중 작은 것을 기준으로 옮길 수 있는 물건의 개수를 판정하였고
해당 물건의 개수만큼 옮길 때 드는 비용을 for문을 이용해 계산하였음
출력에 물건의 개수를 포함하지 않아서 틀렸었음
"""
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
former = [int(input()) for _ in range(n)]
latter = [int(input()) for _ in range(m)]

max_num = min(sum(former), sum(latter))
former_capacity = latter_capacity = max_num
ans = 0
for i in range(n): 
    if former_capacity >= former[i]:
        former_capacity -= former[i]
        ans += former[i] * (i + 1)
    else:
        ans += former_capacity * (i + 1)
        break
    
for i in range(m): 
    if latter_capacity >= latter[i]:
        latter_capacity -= latter[i]
        ans += latter[i] * (i + 1)
    else:
        ans += latter_capacity * (i + 1)
        break
print(max_num, ans)