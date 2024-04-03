"""
이분탐색을 구현해서 풀이하였음
정렬을 하게되면 오름차순으로 된다는 특성을 이용해
큰 값에서부터 작은 값으로 이동하면서 쌍을 지을 수 있는 수의 idx를 저장하면서
다음 수의 쌍을 찾을 때는 해당 수의 idx부터 탐색하면 이분탐색보다 빠른 속도가 나올 것으로 예상됨?
"""
N = int(input())
files = list(map(int, input().split()))
files.sort()

def b_search(n):
    standard = files[n-1]
    left = 0
    right = n-1
    result = None
    while left <= right:
        mid = (left + right) // 2
        if files[mid] >= standard * 0.9:
            result = mid
            right = mid-1
        else:
            left = mid+1
    return n-1-result
ans = 0
for i in range(N, 1, -1):
    ans += b_search(i)
print(ans)