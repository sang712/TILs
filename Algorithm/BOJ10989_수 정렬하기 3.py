'''
처음에 모든 입력을 받아서 list로 만들려고 했더니 메모리 초과가 났음
-> 수의 범위가 1~10000까지여서 10001길이의 리스트를 만들어 해당 값의 count를 높이고
count만큼 idx를 출력하도록 하였음 = 8976ms
-> print를 할 때 for문을 돌지 않고 한번에 출력하도록 print((출력 + '\n')*출력회수) 했더니
'\n'때문에 출력사이의 값에 줄바꿈이 들어감
-> print를 sys.stdout.write로 바꾸니 출력할 때 마지막 줄바꿈이 사라짐, 속도는 비슷하다고 함
대신 이것 역시 메모리초과
-> 특정숫자를 정해 해당 숫자이상 카운트가 되었으면 한번에 그 숫자만큼 반복 출력하도록 하여
한 번에 출력하는 내용물의 양을 조절함
10000번 카운트당 한 번 출력으로 할 때 4548ms, 1000번 카운트당 한 번으로 할 때 4704ms가 소요됨
'''
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
numbers = [0] * 10001
for _ in range(N):
    numbers[int(input())] += 1

for i in range(10001):
    if numbers[i]:
        while numbers[i] > 10000:
            print((str(i) + '\n')*10000)
            numbers[i] -= 10000
        print((str(i) + '\n')*numbers[i])