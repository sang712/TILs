"""
stack 자료구조를 이용해 한번만 돌면서 바로바로 판단할 수 있도록 하였음
왼쪽 괄호만 stack에 넣고 오른쪽 괄호와 쌍이 맞으면 숫자를 더하거나 곱하도록 하였고
숫자 결과도 stack에 같이 넣어 보관하도록 하였음
그래서 만약 괄호 사이에 숫자가 껴 있으면 해당 숫자를 모두 더하도록 하였고
주어진 입력을 모두 확인했으면 stack에 남아있는 왼쪽 괄호를 확인하고
남아있지 않으면 stack에 남은 숫자들을 모두 더해 출력하도록 하였음
"""
parenthesis = input()

stack = []
for s in parenthesis:
    if s == '(' or s == '[':
        stack.append(s)
    elif s == ')':
        temp = 0
        while stack and type(stack[-1]) == int:
            temp += stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
            temp += 2 if temp == 0 else temp
            stack.append(temp)
        else:
            print(0)
            break
    elif s == ']':
        temp = 0 
        while stack and type(stack[-1]) == int:
            temp += stack.pop()
        if stack and stack[-1] == '[':
            stack.pop()
            temp += 3 if temp == 0 else temp * 2
            stack.append(temp)
        else:
            print(0)
            break
else:
    output = 0
    for num in stack:
        if type(num) == int:
            output += num
        else:
            output = 0
            break
    print(output)