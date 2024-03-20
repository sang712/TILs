"""
연속한 구간을 정해서 set함수를 적용시키는 것은 시간이 오래 걸릴 것 같아서
나올 수 경우를 개별 카운팅 하는 방식을 사용하였음
초밥의 종류의 최댓값은 3000가지 이므로 최대 3000인 리스트가 필요하니 메모리 걱정은 안해도 되겠다 생각하였음
우선 k길이 만큼 잘라서 각 초밥의 개수 카운팅을 하였고 선택한 초밥의 가지 수는 또 따로 카운팅하였음
쿠폰이 가지 수 카운팅에 영구적으로 영향을 주게 하지 않기 위해서 최댓값을 계산할 때만 적용하였음
그 후엔 슬라이딩 윈도우 방식으로 맨 앞에 건 제거하고 맨 뒤에 값을 추가하면서 최댓값을 갱신했음
"""
import sys

N, d, k, c = map(int, input().split())
conveyor = []
comb = [0] * (d+1)
for _ in range(N):
    conveyor.append(int(sys.stdin.readline()))
conveyor += conveyor[:k]
cnt = 0
for i in range(k):
    chobap = conveyor[i]
    if comb[chobap] == 0:
        cnt += 1
    comb[chobap] += 1

coupon = 0 if comb[c] else 1
max_cnt = cnt + coupon
for i in range(k, len(conveyor)):
    chobap = conveyor[i-k]
    comb[chobap] -= 1
    if comb[chobap] == 0:
        cnt -= 1
    chobap = conveyor[i]
    if comb[chobap] == 0:
        cnt += 1
    comb[chobap] += 1
    
    coupon = 0 if comb[c] else 1
    max_cnt = max(max_cnt, cnt + coupon)
print(max_cnt)