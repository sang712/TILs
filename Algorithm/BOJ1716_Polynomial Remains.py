"""
입력은 차수가 작은 것부터 들어오기 때문에 이 점에 유의하고 풀었어야 했음
문제를 처음 읽었을 때는 이 부분을 캐치하고 넘어갔는데 구현하다보니 망각하게 되었고
예제가 중간에 하나를 제외하고는 거꾸로 풀어도 같은 값을 가지다보니 제대로 확인하지 않아 틀린답을 제출했었음

우선 while문으로 입력을 받고 입력이 -1, -1이면 멈추고
k가 0이면 무조건 나누어 떨어지므로 0출력
k가 n보다 크거나 같으면 더이상 나눌 수 없으므로 그대로 출력하도록 했고
여기서 또 실수가 있었는데 k값을 비교하기 전에 a를 모두 받아와야 다음 입력을 받아옴에 있어 문제가 없음
"""
import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().split())
    if n == k == -1:
        break
    a = list(map(int, input().split()))
    if k == 0:
        print(0)
        continue
    elif k >= n:
        print(*a)
        continue
    for i in range(n, k-1, -1):
        a[i-k] -= a[i]
        a[i] = 0
    idx = k
    while idx > 0 and a[idx] == 0:
        idx -= 1
    ans = a[:idx+1]
    if ans:
        print(*ans)
    else:
        print(0)