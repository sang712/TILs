"""
길이가 모두 같을 경우 최대의 값이 나오기 때문에 길이가 같아지는 방향으로 풀이하였음
"""
import sys
input = sys.stdin.readline

for t in range(int(input())):
    input()
    *cake_sides, D = map(int, input().split())
    A, B, C = sorted(cake_sides)
    sides = A + B + C - D
    A = min(sides // 3, A)
    sides -= A
    B = min(sides // 2, B)
    C = sides - B
    print(A * B * C)
