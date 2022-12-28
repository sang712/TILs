'''
입력을 받아 연산자가 *면 곱셈을 연산자 +면 덧셈을 하여 출력하도록 하였음
'''
A = int(input())
operator = input()
B = int(input())

print(A * B if operator == '*' else A + B)