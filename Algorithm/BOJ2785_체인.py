"""
가장 짧은 체인에서 고리를 하나를 빼서 가장 긴 체인 2개를 묶는다고 생각하면
마지막 체인은 무시하고 N-1번 엮는다고 생각했음
여기에 추가로 고려해야할 것이
체인의 고리가 체인을 엮는데 사용되어 소모되는 경우
엮어야 되는 체인의 개수가 하나 줄어드는 것으로 생각하면 됨
"""
N = int(input())
chains = list(map(int, input().split()))
chains.sort()

start, end = 0, N-2
ans = 0
while start <= end:
    ans += 1
    if chains[start] > 1:
        chains[start] -= 1
    else:
        start += 1
    end -= 1
print(ans)