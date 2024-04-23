"""
에라토스테네스의 체로 10만까지의 소수를 모두 구하고
소수로 나눠보면서 해당 수로 나뉘면 저장한 뒤에 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

colander = [1] * 100_001
prime_num = []
for num in range(2, 100_001):
    if colander[num]:
        prime_num.append(num)
        for i in range(num, 100_001, num):
            colander[i] = 0
        
for _ in range(int(input())):
    N = int(input())
    ans = []
    for prime in prime_num:
        if N >= prime:
            cnt = 0
            while N % prime == 0:
                N //= prime
                cnt += 1
            if cnt:
                ans.append(f'{prime} {cnt}')
        else:
            break
    print(*ans, sep='\n')