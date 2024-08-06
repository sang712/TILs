"""
양쪽 끝 값의 높이를 더하고 윗면과 아랫면의 넓이를 위해 N을 두 번 더해주고 
앞면과 뒷면의 넓이를 위해 주어진 h값을 두 번씩 더해준 뒤
연속된 h값의 차이의 절댓값을 더해주었음
"""
N = int(input())
h = list(map(int, input().split()))
ans = h[0] + h[-1] + 2 * (N + sum(h))
for i in range(1, N):
    ans += abs(h[i-1] - h[i])
print(ans)