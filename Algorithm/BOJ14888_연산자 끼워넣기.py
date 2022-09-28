'''
재귀를 이용하여 요구하는 사항을 구현 하였음

int(음수/양수)와 (음수//양수)가 다름
int()는 소수점 이하를 버려서 몫만을 취한 결과가 나오는데
음수//양수 는 소수점 이하를 버림(?)floor 해버려서 원하는 값보다 1만큼 작은 값을 얻게 됨
음수를 포함한 나눗셈으로 몫을 구할 경우 int(숫자/숫자)를 이용하는 것으로!!

+) 놀라운 사실, 출력을 한 줄로 출력해도 맞은 답으로 처리가 됨
'''
N = int(input())
A = list(map(int, input().split()))

operators = list(map(int, input().split())) # +, -, *, / 순서

def operate(num1, num2, idx):
    if idx == 0:
        return num1 + num2
    elif idx == 1:
        return num1 - num2
    elif idx == 2:
        return num1 * num2
    elif idx == 3:
        if num1 < 0:
            return -((-num1) // num2)
        return num1 // num2

# 대신 1e9, -1e9와 같이 표현할 수 있음
min_n, max_n = 1000000000, -1000000000
# operators list를 인자로 줬을 때 조금 더 빨랐음 약 8ms
def calculate(num, i): # 숫자, 인덱스, 더하기, 빼기, 곱하기, 나누기
    global min_n, max_n
    if i < N:
        for idx, times in enumerate(operators):
            if times > 0:
                operators[idx] -= 1
                calculate(operate(num, A[i], idx), i+1)
                operators[idx] += 1
    else:
        min_n = min(min_n, num)
        max_n = max(max_n, num)
        
calculate(A[0], 1)
print(max_n)
print(min_n)