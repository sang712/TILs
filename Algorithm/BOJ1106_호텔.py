"""
배낭 문제를 푸는 방식으로 풀이하였음
우선 최소값을 구하는 문제이므로 기준이 되는 기준값을 0이 아닌 C * 101로 잡았는데
이는 최대 인원수 * (최대 비용 + 1) 임 
+) 최대 인원수 * 최대 비용 + 1 해도 되긴 하는 거 같음

그리고 도시별(i)로 홍보로 증가시키려는 고객 수(j)를 1씩 늘려가며 필요한 최소한의 비용을 계산하였고
(cost_for_this_ad[j - customer] + cost)
확인하려는 고객 수(j)가 홍보 한 번으로 증가하는 고객의 수(customer)보다 작으면 
그냥 비교없이 직전 도시에서 계산한 최소한의 비용을 사용하였음

배낭 문제인데 최소값을 구하는 응용 문제임 
최소값을 구하는 문제이므로 기준값을 넣어주어야 한다는 점과
그에 따라 파생된 "적어도 C명"이라는 조건을 해결하기 위해 배낭의 범위를
C + 1이 아닌 C + 101로 설정한 점
또 그에 따라 출력을 min(배낭[N][-101:]) 로 해야했던 점들이 이 문제를 풀기위해 추가 변형된 점임
"""
import sys
input = sys.stdin.readline

C, N = map(int, input().split())

ads = [tuple(map(int, input().split())) for _ in range(N)]
cost_per_customer = [[C * 101] * (C + 101)]

for i in range(N):
    cost, customer = ads[i]
    cost_for_this_ad = [0]
    for j in range(1, C + 101):
        if j >= customer:
            current = min(cost_per_customer[i][j], cost_for_this_ad[j - customer] + cost)
        else:
            current = cost_per_customer[i][j]
        cost_for_this_ad.append(current)
    cost_per_customer.append(cost_for_this_ad)

print(min(cost_per_customer[N][-101:]))