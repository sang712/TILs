"""
이분 탐색이래서 쉽게 생각했더니 시간초과가 나는 경우가 있었음

보통 내가 접한 이분 탐색의 경우는 정수 범위에서 끝나는데 이 문제는 소수점 9째자리까지 오차를 확인한다고 해서
mid를 구하는 부분에서 // 가 아닌 / 를 사용해야 했고
left와 right를 초기화 하는 부분에서도 0.000_000_001을 사용하였음

그리고 while left <= right 를
while right - left <= 0.000_000_001로 수정하려고 하다가
어떤 경우에서는 이 구문이 항상 참일 수도 있다고 해서
for문으로 바꿔서 해결했음

100회 이상의 반복이 예상되는 이분 탐색에서는 for문을 사용하는 것 고려해봐야 한다는 것을 알게 되었음
"""
N, L, W, H = map(int, input().split())

def is_fit(A):
    l = L // A
    w = W // A
    h = H // A
    if l * w * h >= N:
        return True
    return False

ans = 0
left, right = 0, 1_000_000_000
for _ in range(70):
    mid = (left + right) / 2
    if is_fit(mid):
        left = mid + 0.000_000_001
        ans = max(mid, ans)
    else:
        right = mid - 0.000_000_001
print(ans)