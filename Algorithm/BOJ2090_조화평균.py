"""
조화평균의 분자는 덧셈, 분모는 곱셈
조화 평균을 구하기 위해서는 통분하는 과정이 필요해서 모든 수의 최대공약수를 구했음
분수의 덧셈에서 분모는 최소공배수이기 때문에 모든 수를 곱한 뒤 최대공약수로 N-1번 나눠주었고
분수의 덧셈에서 분자는 분자에 분모를 최소공배수로 만들기 위한 값을 곱한 것이므로
최대공약수 나누기 해당 수를 곱하는 방식으로 구하였음(문제에서 각 분수의 분자는 1)

최대공약수(gcd): greatest common divisor
약분: commensuration
통분: reduction to a common denominator
"""
N = int(input())
nums = list(map(int, input().split()))

def gcd(num1, num2):
    if num2 == 0: return num1
    else: return gcd(num2, num1%num2)
common_divisor = nums[0]
for i in range(1, N):
    common_divisor = gcd(common_divisor, nums[i])
    
numerator = nums[0]
for i in range(1, N):
    numerator *= nums[i] // common_divisor

denominator = 0
for i in range(N):
    denominator += numerator // nums[i]
    
factor = gcd(numerator, denominator)
print(f'{numerator//factor}/{denominator//factor}')