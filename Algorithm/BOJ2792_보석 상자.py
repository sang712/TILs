"""
이분 탐색을 적용하여 풀었고
많은 연습을 했던 매개 변수 탐색 방식을 이용해 풀었음
처음에 1500ms가 나왔고 다른 풀이는 1000ms 정도길래 함수 내부 로직을 바꿔 봤는데
divmod 보다 그냥 // % 연산으로 각각 처리하는 게 오히려 더 빠르다는 것을 알게 되었음
그리고 for문 안에서 제한 조건을 체크하는 것 보다 밖에서 체크하는 것이 약간 더 빠르다는 것도 알게 되었음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
jewels = [int(input()) for _ in range(M)]

def devide(jealous):
    num_students = 0
    for jewel in jewels:
        num_students += jewel//jealous
        num_students += 1 if jewel%jealous else 0
    if num_students <= N:
        return True
    return False

left, right = 1, 1_000_000_000
ans = 1_000_000_000
while left <= right:
    mid = (left + right) // 2
    if devide(mid):
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
print(ans)