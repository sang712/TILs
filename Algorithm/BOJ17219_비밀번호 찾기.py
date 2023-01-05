'''
readline으로 입력을 받으면 무조건 split이나 strip으로 '\n'을 제거해 주어야 한다는 점 유의할 것
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

password_of = {}

for _ in range(N):
    website, password = input().split()
    password_of[website] = password

for _ in range(M):
    print(password_of[input().strip()])