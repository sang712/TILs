'''
정렬하는 과정에서 나이(숫자)를 int가 아닌 str형식으로 입력을 받았기 때문에
9와 10의 우선순위 중 10을 먼저 우선으로 잡기 때문에 틀렸었음
앞으로는 정렬을 할 때 숫자는 int인지 아닌지를 먼저 확인할 것
'''
import sys
input = sys.stdin.readline

N = int(input())
users = []
for i in range(N):
    users.append([*input().split(), i])
users.sort(key=lambda x: (int(x[0]), x[2]))

for i in range(N):
    print(f'{users[i][0]} {users[i][1]}')
