"""
이분 탐색 문제임을 파악하고 최근에 연습한 것을 토대로 쉽게 풀이할 수 있었음
다만 이번에 느낀 것은 이분 탐색 문제를 풀이할 때 주의해야 할 점인데
첫째는 left, right 값을 잘 설정해야 한다는 것임
~여기서는 0 + mid / X + mid 에서 X와 mid(가 될 수 있는 값)이 최대 일 때 1퍼센트를 띄우려면~
10^7보단 크고 10^8보단 작은 값을 사용하면 최적화가 될 줄 알았는데 틀린 답을 얻게 됨
둘째로 ans이 될 값이 무엇인지를 잘 설정해야함
횟수라고 해서 그냥 조건을 만족할 때마다 ans += 1을 했었는데 이것은 틀린 것이었고
ans = mid로 해주었음
"""
X, Y = map(int, input().split())

Z = Y * 100 // X

left = 1
right = 1_000_000_000
ans = -1
while left <= right:
    mid = (left + right) // 2
    new_Z = (Y + mid) * 100 // (X + mid)
    if Z == new_Z:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid
        
print(ans)