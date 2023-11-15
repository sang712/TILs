import sys
input = sys.stdin.readline 

T = int(input())
num = 0
for _ in range(T):
    _ = input()
    N = int(input())
    for _ in range(N):
        num += int(input())
        
    if num % N == 0 or num == 0:
        print('YES')
    else:
        print('NO')
    num = 0