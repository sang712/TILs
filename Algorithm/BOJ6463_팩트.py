"""
10000 이하의 값을 곱하면서 생길 수 있는 0의 최대의 개수는 4개이고
이 0들에 영향을 받지 않으면서 연산속도를 개선하기 위해
가져야할 유효숫자의 자리수는 5자리이므로 100_000으로 나누어 주었음
"""
import sys
input = sys.stdin.readline

fact = [1]
try:
    while True:
        N = int(input())
        if len(fact) <= N:
            for i in range(len(fact), N+1):
                last_num = fact[-1]
                last_num *= i
                while True:
                    if last_num%10:
                        fact.append(last_num%100000)
                        break
                    else:
                        last_num //= 10
        print(f'{N:>5} -> {str(fact[N])[-1]}')
except:
    pass
