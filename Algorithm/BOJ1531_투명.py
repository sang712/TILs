"""
입력을 받아 100*100 격자위에 해당하는 칸마다 1씩 더해주었고
해당 수가 M을 초과하는 경우만 더하여 출력하도록 하였음
M을 초과하는 경우를 찾는 방법으로는 map함수에 lambda를 사용하였음
M보다 크면 True를 반환하여 True혹은 False를 원소로 갖는 map객체를 반환하게되며 
이를 sum의 인자로 넣었을 땐 True를 1로 취급하기 때문에 해당 방법으로 진행하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
image = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    
    for r in range(x1 - 1, x2):
        for c in range(y1 - 1, y2):
            image[r][c] += 1

blurred_pixel = 0
for row in image:
    blurred_pixel += sum(map(lambda x: x > M, row))

print(blurred_pixel)