'''
재귀를 이용해 계산을 하도록 하였음
이 때 유의점은 지수가 짝수일 때 함수를 2번 호출하지 않도록 해야 한다는 것이고
따로 변수를 선언해 호출한 값을 저장하였음
'''
A, B, C = map(int, input().split())

def square(num, exp, denom):
    if exp == 1:
        return num % denom
    if exp % 2:
        return (num * square(num, exp-1, denom)) % denom
    else:
        temp = square(num, exp//2, denom) % denom
        return (temp * temp) % denom

print(square(A, B, C))