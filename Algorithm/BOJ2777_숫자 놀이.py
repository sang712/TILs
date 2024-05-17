"""
10보다 작은 수로 나누어 떨어지는 경우에만 x가 존재하고 그렇지 않은 경우는 -1을 출력하도록 하였음
n이 1인 경우를 제외하고는 1이 자릿수에 사용되는 것은 무의미하기 때문에 구현에 사용하지 않았는데
n이 1인 경우를 예외처리 해주었음
"""
import sys
input = sys.stdin.readline

for t in range(int(input())):
    num = int(input())
    if num == 1:
        print(1)
        continue
    x = []
    for i in range(9, 1, -1):
        while True:
            if num % i == 0:
                x.append(i)
                num //= i
            else:
                break
    if num > 1:
        print(-1)
    else:
        print(len(x))