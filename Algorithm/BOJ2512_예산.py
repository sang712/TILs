"""
전형적인 이분 탐색 문제
단 시작 최댓값을 지역별 요구 예산의 최댓값으로 설정하지 않으면 결과 값이 끝도 없이 올라갈 수 있음
"""
N = int(input())
regions = list(map(int, input().split()))
budget = int(input())

def allocate(money):
    consumed = sum(map(lambda x: min(x, money), regions))
    if consumed <= budget:
        return True
    return False

left, right = 0, max(regions)
ans = 0
while left <= right:
    mid = (left + right) // 2
    if allocate(mid):
        left = mid + 1
        ans = max(mid, ans)
    else:
        right = mid - 1
print(ans)