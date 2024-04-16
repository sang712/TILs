"""
직교다각형이 이루어지는 경우만 입력으로 들어온다고 했으니 
같은 x값을 가지는 점과 같은 y값을 가지는 점은 모두 짝수라고 판단을 했음 두 점이 있어야 직선이 되므로
그 후에는 dictionary 자료 구조에 x값별 y값과 y값별 x값을 각각 저장한 뒤에
해당 딕셔너리를 반복문으로 돌면서 2개씩 pop하면서 큰 값에서 작은 값을 빼는 방식으로 길이를 구하였음
"""
import sys
input = sys.stdin.readline
N = int(input())
x_of_y = {}
y_of_x = {}
for _ in range(N):
    x, y = map(int, input().split())
    y_of_x.setdefault(x, [])
    y_of_x[x].append(y)
    x_of_y.setdefault(y, [])
    x_of_y[y].append(x)

length = 0
for y in x_of_y:
    x_poses = sorted(x_of_y[y])
    while x_poses:
        length += x_poses.pop() - x_poses.pop()
for x in y_of_x:
    y_poses = sorted(y_of_x[x])
    while y_poses:
        length += y_poses.pop() - y_poses.pop()
print(length)