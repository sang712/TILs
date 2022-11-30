'''
주어진 조건이 5000이라서 
구현한 코드의 시간복잡도 O(N^2)을 고려했을 때 통과할 줄 알았는데
min max를 여러번 쓰다보니 많은 시간을 소요한 듯 하다
그래서 pypy3를 적용하여 통과하였음

파이썬으로 통과한 코드를 살펴보고 해당 방식으로 구현하여 통과하였음
차이점은 매 for문을 돌 때마다 min, max를 사용하는 것이 아니라
한 idx에서 해결가능한 모든 경우의 수를 구해서 한번에 적용하는 것
이렇게 하면 연산의 회수를 줄일 수 있어서 python으로도 통과가 가능한 듯

+) 추가로 생각해볼 지점이 
내가 구현한 코드는 dp라기보다 브루트 포스같다는 느낌임
참고했던 코드는 순차적으로 idx를 1개씩 늘려가며 
해당 지점까지의 경우의 수를 모두 계산한 뒤에 다음 idx로 넘어간 반면
나는 처음부터 끝까지 계산하고, idx 한 칸 뒤부터 계산하는 방식으로 진행해서
dp의 의미? 와는 사뭇 달라진 코딩 방식이었던 것 같음
'''
# pypy3 324ms 소요된 코드
'''
N = int(input())
A = list(map(int, input().split()))

MAX = float('inf')
dp = [MAX] * N

for j in range(1, N):
    dp[j] = min(dp[j], (j - 0) * (1 + abs(A[0] - A[j])))
    
for i in range(1, N):
    for j in range(i+1, N):
        to_j = max(dp[i], (j - i) * (1 + abs(A[i] - A[j])))
        dp[j] = min(dp[j], to_j)
print(dp[-1])
'''
# python 통과 기원 코드
N = int(input())
A = list(map(int, input().split()))

dp = [0] * N

for j in range(1, N):
    max_to_j = []
    for i in range(0, j):
        max_to_j.append(max(dp[i], (j - i) * (1 + abs(A[i] - A[j]))))
    dp[j] = min(max_to_j)
print(dp[-1])