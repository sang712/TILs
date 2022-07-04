import sys
input = sys.stdin.readline

N = int(input())

triangle = [0 for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(len(line)-1, -1, -1):
        if j == 0:
            triangle[j] += line[j]
        elif 0 < j < len(line)-1:
            triangle[j] = max(triangle[j-1], triangle[j]) + line[j]
        else:
            triangle[j] = triangle[j-1] + line[j]
print(max(triangle))

'''
<다른 풀이>

왼쪽에 0을 추가한 줄과 오른쪽에 0을 추가한 줄, input 값을 zip()으로 묶음
왼쪽에 0을 추가한 줄과 오른쪽에 0을 추가한 줄은 트리의 좌, 우 값을 갖게 됨
해당 값을 비교함으로써 max 값을 선택할 수 있고 zip()으로 묶은 값만을 더하면 끝
'''
'''
import sys
n = int(input())
dp_n = []

for _ in range(n):
    dp_b = list(map(int, sys.stdin.readline().split()))
    dp_cache = []
    for n_t1, n_t2, n_b1 in zip([0]+dp_n, dp_n+[0], dp_b):
        print("print: ", n_t1, n_t2, n_b1)
        dp_cache.append(max(n_t1, n_t2) + n_b1)
    dp_n = dp_cache
print(max(dp_n))
'''
'''
import sys
read = sys.stdin.readline

n = int(read())
cache = []

for i in range(n):
    floor = list(map(int, read().split()))
    cache = [max(a+c, b+c) for a, b, c in zip([0]+cache, cache+[0], floor)]
print(max(cache))
'''