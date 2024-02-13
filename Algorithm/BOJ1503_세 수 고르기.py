"""
처음 문제는 for문의 범위를 1001까지로 했기 때문임
집합의 원소의 조건으로 자연수 1000까지라 1001은 범접할 수 없기 때문에
1이 살아있다면 1001도 고려를 해주어야 함

브레이크를 거는 i*j>N, i>N에서 문제가 생겼다고 판단했는데 그게 아니라
ans가 갖고 있는 값이 문제였음 입력으로 주어진 집합이 1부터 50까지였으면
이미 |N-xyz|가 1000을 넘긴상태라 ans는 갱신이 되지 않음

브레이크 문은 이미 먼저 확인을 다 하고 
그 다음 숫자를 확인하지 않기 위한 수단으로 사용되었기 때문에 유효
"""
N, M = map(int, input().split())
nums = set(map(int, input().split()))
ans = 132_652
for i in range(1, 1002):
    if i in nums:
        continue
    for j in range(i, 1002):
        if j in nums:
            continue
        for k in range(j, 1002):
            if k in nums:
                continue
            temp = i*j*k
            ans = min(ans, abs(N-temp))
            if temp > N:
                break
        if i*j > N:
            break
    if i > N:
        break
print(ans)