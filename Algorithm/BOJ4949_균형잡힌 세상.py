'''
요구사항대로 구현하였음
마지막 입력의 의미의 '.'을 처리하지 않은 것이 문제였는데 처리를 하여 해결하였음
'''
while True:
  string = input()
  if string == '.':
    break
  stack = []
  for char in string:
    length = len(stack)
    if char == '(':
      stack.append('(')
    elif char == '[':
      stack.append('[')
    elif char == ')':
      if length > 0 and stack[length-1] == '(':
        stack.pop(length-1)
      else:
        print("no")
        break
    elif char == ']':
      if length > 0 and stack[length-1] == '[':
        stack.pop(length-1)
      else:
        print("no")
        break
    elif char == '.':
      if len(stack) == 0:
        print("yes")
        break
      else:
        print("no")
        break
