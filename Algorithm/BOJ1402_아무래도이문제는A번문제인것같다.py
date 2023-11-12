"""
어떤 숫자를 만드는 곱이든 더했을 때 짝수, 홀수를 둘 다 만들 수 있으면 무조건 yes임
예를 들어 7을 7, 7*1 로 만들면 더했을 때 7, 8 로 홀수, 짝수를 만들 수 있음
이 때 짝수개의 -1, 혹은 1을 곱해주면 어떤 수든 만들 수 있음

그런데 어떤 수 n이든 n과 n*1로 n을 만들 수 있으므로 더했을 때 홀수, 짝수 모두 만들 수 있음
따라서 모든 입력에 yes를 출력하면 됨
"""
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    _ = input()
    
ans = ['yes'] * T
print(*ans, sep='\n')