"""
순열을 모두 완성하고 값을 계산하면 python3에서 시간초과가 나서
중간과정에 계산한 포션 값이 이제까지 나온 값보다 크면 중단하는 방식으로 프루닝 하였음
pypy3 2500ms에서 1100ms로 줄였고 python3는 시간초과에서 7800ms, 그리고 6800ms로 단축하였음

단축하는 방법에서 방문처리를 비트마스킹으로 처리하면 
메모리측면과 속도 측면에서 엄청난 개선이 있는 것 같아서 해당 방법을 찾아봐야겠음
"""
import sys
input = sys.stdin.readline

N = int(input())
ci = [0] + list(map(int, input().split()))
pi = [[]]
for _ in range(N):
    temp = []
    for _ in range(int(input())):
        a, d = map(int, input().split())
        temp.append((a, d))
    pi.append(temp)

bought = [0] * (N+1)
discount = [0] * (N+1)

ans = 1000 * N
def buy_nth_potion(n, cost):
    global ans
    if n > N:
        ans = min(ans, cost)
        return
    
    for i in range(1, N+1):
        if bought[i]:
            continue
        pay = max(1, ci[i]-discount[i])
        if cost + pay > ans:
            continue
        bought[i] = 1
        for aj, dj in pi[i]:
            discount[aj] += dj
        buy_nth_potion(n+1, cost + pay)
        for aj, dj in pi[i]:
            discount[aj] -= dj
        bought[i] = 0
buy_nth_potion(1, 0)
print(ans)