"""
나무 사이의 거리 중 가장 작은 값을 사용하면 되는 줄 알았는데 그것이 아니고
나무 사이의 거리의 최대공약수를 구해서 그 간격별로 떨어져 있는 부분을 카운팅하면 되는 문제였음
그리하여 나무 사이의 거리의 최대공약수를 구한 뒤에
가장 멀리 떨어진 나무와 가장 가까운 나무의 거리를 구해서 최대공약수로 나누어 주었고
그 사이에 현재 심어진 나무가 N개니까 몫에서 N개를 빼 주었음
근데 사이 라는 값이 첫값이나 끝값 어느 하나를 포함하지 않으므로 
1을 덜 빼야하기 때문에 1을 더해주고 출력하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
trees = [int(input()) for _ in range(N)]

def gcd(num1, num2):
    if num2 == 0: return num1
    else: return gcd(num2, num1%num2)

gap = trees[1]-trees[0]
for i in range(2, N):
    gap = gcd(gap, trees[i] - trees[i-1])
    if gap == 1:
        break
print((trees[N-1] - trees[0]) // gap - N + 1)