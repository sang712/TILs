"""
픽셀로 이루어진 이미지를 입력받아 중앙값을 반환하는 3*3필터를 통과시킨 픽셀 중
조건보다 크거나 같은 픽셀의 수를 반환하는 문제
문제에서 요구한대로 필터의 크기만큼 기존 이미지에서 픽셀을 가져와 정렬하고
중앙값을 추출해 T와 비교한 뒤에 카운팅하였음
"""
import sys
input = sys.stdin.readline

R, C = map(int, input().split())

image = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

answer = 0
for r in range(R - 2):
    for c in range(C - 2):
        filtered_pixel = []
        filtered_pixel.extend(image[r][c:c + 3])
        filtered_pixel.extend(image[r + 1][c:c + 3])
        filtered_pixel.extend(image[r + 2][c:c + 3])
        filtered_pixel.sort()
        answer += 1 if filtered_pixel[4] >= T else 0
        
print(answer)