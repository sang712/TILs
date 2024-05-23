"""
2부터 L까지 반복하면서 K를 나누어 떨어뜨릴 수 있는지 확인하는 방법으로 풀이하였음
"""
K, L = map(int, input().split())
for i in range(2, L):
    if K % i == 0:
        print('BAD', i)
        break
else:
    print('GOOD')