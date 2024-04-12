"""
식을 입력을 받아서 반복문으로 돌면서 중위연산으로 연산을 하면서
알파벳으로 들어온 숫자를 순서대로 들어온 숫자로 변환하여 적용하도록 구현하였음
"""
import sys
N = int(input())
formula = input()
nums = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
for element in formula:
    if element == '+':
        stack.append(stack.pop() + stack.pop())
    elif element == '-':
        latter = stack.pop()
        stack.append(stack.pop() - latter)
    elif element == '*':
        stack.append(stack.pop() * stack.pop())
    elif element == '/':
        latter = stack.pop()
        stack.append(stack.pop() / latter)
    else:
        stack.append(nums[ord(element) - ord('A')])
print(f'{stack[0]:.2f}')