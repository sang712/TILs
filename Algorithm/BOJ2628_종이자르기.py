"""
주어진 입력을 가로 자르기, 세로 자르기로 나눠서 받았고
그것을 0과 세로, 0과 가로를 포함시켜 정렬한 뒤
각각의 원소의 차이가 가장 큰 부분을 구해 곱하여 출력하였음

주의할 점은, 가로로 잘랐을 때는 세로의 길이가 나오고
세로로 잘랐을 때는 가로의 길이가 나온다는 것임
"""
width, height = map(int, input().split())
N = int(input())
hor_cut = [0, height]
ver_cut = [0, width]
for _ in range(N):
    hv, point = map(int, input().split())
    if hv:
        ver_cut.append(point)
    else:
        hor_cut.append(point)
ver_cut.sort()
hor_cut.sort()
max_width = max_height = 0
for i in range(1, len(hor_cut)):
    max_height = max(max_height, hor_cut[i] - hor_cut[i-1])
for i in range(1, len(ver_cut)):
    max_width = max(max_width, ver_cut[i] - ver_cut[i-1])
print(max_height * max_width)