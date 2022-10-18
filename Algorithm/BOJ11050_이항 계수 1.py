'''
팩토리얼이라 겹치는 수가 없으므로 set으로 둘 수 있었음, 
곱하는 수와 나누는 수가 겹치면 계산하기 전에 없애버리기 위해 set을 사용
오히려 계산을 반복하는 것일 수도
'''
N, K = map(int, input().split())

multiply = set(i for i in range(1, N+1))

devide1 = set(i for i in range(1, K+1))
devide2 = set(i for i in range(1, N-K+1))

temp = multiply & devide1
multiply -= temp
devide1 -= temp

temp = multiply & devide2
multiply -= temp
devide2 -= temp

ans = 1
for i in multiply:
    ans *= i
for i in devide1:
    ans /= i
for i in devide2:
    ans /= i
print(int(ans))