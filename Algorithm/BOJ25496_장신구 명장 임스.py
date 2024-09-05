"""
피로도가 200 미만일 경우 제작이 가능하다는 점에 유의하여 풀이하였음
"""
P, N = map(int, input().split())
ans = 0
accessories = list(map(int, input().split()))
accessories.sort()
for i in accessories:
    if P < 200:
        ans += 1
        P += i
    else:
        break
print(ans)
