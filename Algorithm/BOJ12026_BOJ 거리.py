'''
굳이 어렵게 B, O, J의 경우 나눌 필요 없이
길이가 최대 1000이므로 2중 for문을 이용하면 1,000,000번이므로 쉽게 풀 수 있었음
처음 dp를 원소를 무한대로 갖는 N길이의 리스트로 만들고 0번만 새로 초기화 한 후에
min을 계산값과 비교하여 초기화하는 방법을 이용하였음
'''
N = int(input())
road = input()

dp = [float('inf')] * N

def next_mark(mark):
    if mark == 'B':
        return 'O'
    if mark == 'O':
        return 'J'
    if mark == 'J':
        return 'B'
    
dp[0] = 0

for i in range(N):
    next = next_mark(road[i])
    for j in range(i+1, N):
        if road[j] == next:
            dp[j] = min(dp[i] + (j - i) ** 2, dp[j])

print(-1) if dp[-1] == float('inf') else print(dp[-1])
