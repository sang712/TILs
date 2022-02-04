import sys
input = sys.stdin.readline

n = int(input())
stack = []
max_height = 0
count = 0
for _ in range(n):
    width, height = map(int, input().split())
    while len(stack) > 0 and stack[-1] > height: # 높이가 낮아지면
        count += 1
        stack.pop()
    if len(stack) > 0 and stack[-1] == height: # 같은 높이이면
        continue
    stack.append(height)

while len(stack)>0: # 높이가 높아지다 끝나면
    if stack[-1] >0:
        count+=1
    stack.pop()
print(count)