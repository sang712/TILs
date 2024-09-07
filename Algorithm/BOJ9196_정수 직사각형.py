"""
문제에서 제시한 범위가 크지 않기 때문에 가능한 모든 사각형
주어진 사각형의 최대 크기는  99*100 이며 이 때 대각선의 크기는
/19801이고 이 때 가장 길쭉한 직사각형을 만들면 1과 140.x가 됨
혹시몰라 넉넉잡아 150으로 두고 가능한 모든 넓은 정수 직사각형을 만들어 정렬을 한 뒤
입력값에서 인덱스 하나가 큰 직사각형을 찾아 출력하였음
"""
import sys
input = sys.stdin.readline
ractangles = [(i, j) for i in range(1, 150) for j in range(i+1, 151)]
ractangles.sort(key=lambda r: (r[0]**2 + r[1]**2, r[0]))
while True:
    h, w = map(int, input().split())
    if h == w == 0:
        break
    print(*ractangles[ractangles.index((h, w))+1])
