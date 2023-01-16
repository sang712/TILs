'''
처음에 문제에서 나온대로 구현을 하려고 했다가 시간초과가 나서 질문에 올라온 시간초과 질문들을 확인했음
그래서 시간초과는 주어진 명령 횟수만큼 뒤집는 과정에서 발생한 것을 알게 되어서 
뒤집는 명령이 들어오면 그에따라 True, False 값을 XOR 연산으로 변환하면서 체크함
리스트의 원소를 지우는 명령이 들어왔을 때는 체크했던 True, False 값을 기준으로 
앞에서 지울지 뒤에서 지울지 결정하여 지웠음
마지막에는 체크했던 True, False 값에 따라 뒤집어서 프린트 하도록 함
error 출력은 처음 input 값을 받아올 때 D의 개수를 세서 input의 길이보다 크면 출력하도록 함

220ms 소요됨

2배 빠른 코드를 찾았는데 88ms 소요됨
주어진 정수 배열을 list로의 변환 없이 str형태로 그대로 사용하고 있었음
명령어를 'R'로 스플릿 한 뒤 map함수와 len()함수를 이용해 D의 개수를 따로 카운팅하지 않고 카운팅 되도록 하였음
그 후에 리스트 슬라이싱으로 2칸씩 잘라서(짝수 idx는 앞에서 지우기, 홀수 idx는 뒤에서 지우기 이므로) 
원소를 합한 뒤에 리스트 슬라이싱으로 [짝수 idx 값의 합: 홀수 idx 값의 합]으로 자르는 방법을 사용했음
map에 len()함수를 사용한 것도 신박하고 'R'로 split을 하여 따로 R을 카운팅하지 않아도 됐던 것도 신박했음
여러모로 깔끔한 풀이라고 생각함

알게된 점
* split()을 하면 list로 반환된다는 점
* ^ 는 XOR 연산자로 두 값이 같으면 True 다르면 False를 반환한다는 점
'''
import sys
from collections import deque

input = sys.stdin.readline

for i in range(int(input())):
    p = input().replace('RR', '')
    num_D = p.count('D')
    
    n = int(input())
    if n:
        x = deque(input().strip('[]\n').split(','))
    else:
        x = input()
        x = []
    
    if n >= num_D:
        i = 0
        flipped = False
        while i < len(p):
            if p[i] == 'R':
                flipped ^= True
            elif p[i] == 'D':
                if flipped:
                    x.pop()
                else:
                    x.popleft()
            i += 1
        if flipped:
            x.reverse()
        print('[' + ','.join(x) + ']')
    else:
        print('error')

# 2배 빠른 코드
'''
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    commands = [*map(len, input().rstrip().replace("RR", "").split("R"))]
    is_flip = (len(commands) + 1) % 2

    n = int(input())
    if n == 0:
        input()
        arr = []
    else:
        arr = input().strip("[]\n").split(",")

    front = sum(commands[0::2])
    try:
        back = sum(commands[1::2])
    except:
        back = 0


    if front + back > n:
        print("error")
        continue
    else:
        arr = arr[front:(n-back)]

    if is_flip:
        arr.reverse()
    print(f'[{",".join(arr)}]')
'''