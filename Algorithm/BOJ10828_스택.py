'''
오래전에 연속으로 틀려서 놔둔 문제인데
메모리 고려하겠답시고 처음 스택 길이를 N//2로 잡아 버려서 IndexError가 났던 것이었다
해당 부분 수정하니 성공
추가로 python3는 readline을 사용해도 시간초과가 났다
'''
import sys
imput = sys.stdin.readline

N = int(input())
stack = [0]*N
top = -1
output = ''
for _ in range(N):
    order = input()
    if order == 'top':
        output += (str(stack[top]) if top > -1 else str(top)) + '\n'
    elif order == 'size':
        output += str(top+1) + '\n'
    elif order == 'empty':
        output += ('1' if top == -1 else '0') + '\n'
    elif order == 'pop':
        if top > -1:
            output += str(stack[top]) + '\n'
            top -= 1
        else:
            output += str(top) + '\n'
    else:
        order, num = order.split()
        top += 1
        stack[top] = num

print(output)