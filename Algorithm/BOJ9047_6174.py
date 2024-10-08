"""
입력을 받아서 6174인지 확인하고
Kaprekar 연산을 하고 1000단위가 나올 때까지 앞에 '0'을 추가하였음
"""
N = int(input())
for _ in range(N):
    cnt = 0
    num = input()
    while cnt < 10:
        if num == '6174':
            print(cnt)
            break
        num = sorted(num)
        num = str(int(''.join(num[::-1])) - int(''.join(num)))
        num = '0' * (4-len(num)) + num
        cnt += 1
