"""
가장 짧은 체인에서 고리를 하나를 빼서 가장 긴 체인 2개를 묶는다고 생각하면
마지막 체인은 무시하고 N-1번 엮는다고 생각했음
여기에 추가로 고려해야할 것이
체인의 고리가 체인을 엮는데 사용되어 소모되는 경우
엮어야 되는 체인의 개수가 하나 줄어드는 것으로 생각하면 됨

첫 풀이는 476ms 걸렸는데
두번째 풀이는 312ms 걸리게 하였음

일일이 하나하나 확인하는 것이 아니라
가장 짧은 체인의 고리의 개수를 한번에 연산하는 방식으로 수정하였음
"""
N = int(input())
chains = list(map(int, input().split()))
chains.sort()

# 첫 풀이
# start, end = 0, N-2
# ans = 0
# while start <= end:
#     ans += 1
#     if chains[start] > 1:
#         chains[start] -= 1
#     else:
#         start += 1
#     end -= 1
# print(ans)

num_coupling = N-1
ans = 0
for chain in chains:
    if chain >= num_coupling:
        ans += num_coupling
        break
    else:
        ans += chain
        num_coupling -= chain + 1
print(ans)