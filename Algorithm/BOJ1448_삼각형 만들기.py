"""
삼각형의 세 변의 합이 최대로 만들기 위해 가장 긴 변부터 가장 긴 순서대로 선택하고
선택한 이 변으로 삼각형을 만들기 위해서는 나머지 두 변의 합이 이 변보다 길어야 하며
맨 위의 전제조건을 만족해야하니 각 선택한 변 당 1가지 경우밖에 나오지 않아서 
그리디로 문제를 풀 수 있음
"""
import sys
input = sys.stdin.readline
N = int(input())

sides = [int(input()) for _ in range(N)]
sides.sort(reverse=True)

for i in range(N-2):
    if sides[i] < sides[i+1] + sides[i+2]:
        print(sides[i] + sides[i+1] + sides[i+2])
        break
else:
    print(-1)