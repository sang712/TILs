'''
BOJ10986과 같은 유형

acc = [0 for _ in range(d)] 보다
acc = [0]*d가 조금 더 빠르다

acc에 더할 때마다 cnt에 더해주면 전체에서 2개를 순서없이 고르는 경우의 수와 같다..!
(acc에 더하기 전에 더해주어야 함)
대박인 수학적 사실...
하지만 BOJ10986에 적용했을 땐 오히려 시간이 늘어났음...
'''
import sys
input = sys.stdin.readline

c = int(input())
for tc in range(c):
    d, n = map(int, input().split())
    acc = [0]*d
    acc[0] = 1
    
    sq = list(map(int, input().split()))
    sum = 0
    cnt = 0
    for num in sq:
        sum = (sum + num) % d
        cnt += acc[sum]
        acc[sum] += 1
    
    # cnt = 0
    # for num in acc:
    #     cnt += (num * (num-1)) //2
    print(cnt)