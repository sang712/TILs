"""
분모를 하나씩 계산해 나갈 때, 분모의 분수의 계산 형태는
분모의 배수 + 분모로 나누어 떨어지지 않는 수 이기 때문에
더해서 나오는 가분수도 또한 나누어 떨어지지 않고
따라서 계산 결과(위의 결과의 분자,분모를 뒤집은)로 나오는 분수도 또한 기약분수라는 점
"""
N = int(input())
As = map(int, input().split()[::-1])

denominator = 1
numerator = 0
for a in As:
    denominator, numerator = a * denominator + numerator, denominator

print(denominator - numerator, denominator)