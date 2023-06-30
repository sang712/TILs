import sys
input = sys.stdin.readline

for t in range(int(input())):
    N, M = map(int, input().split())
    X = int(''.join(input().split()))
    Y = int(''.join(input().split()))
    
    serial_num = input().split() * 2
    
    cnt = 0
    for i in range(N):
        num = int(''.join(serial_num[i:i+M]))
        if X <= num <= Y:
            cnt += 1
    print(cnt)