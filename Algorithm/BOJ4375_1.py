def solution(n):
    if n % 2 == 0 or n % 5 == 0:
        return -1
    num = 1
    cnt = 1
    while True:
        if num % n == 0:
            return cnt
        num = num * 10 + 1
        # num = ((num%n) * (10%n) + 1)%n 이 훨신 계산속도가 빠름
        cnt += 1

while True:
    try:
        n = int(input())
        print(solution(n))
    except EOFError:
        break