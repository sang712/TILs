"""
우선 A진법으로 표현한 숫자가 10진법으로 어떻게 되는지 변환한 뒤에
다시 그 수를 B진법으로 표현하기 위해 B로 나눠 저장하였고
그 수를 출력하였음
"""
A, B = map(int, input().split())

m = int(input())
digits_A = list(map(int, input().split()))
the_number = 0
for digit in digits_A:
    the_number = the_number * A + digit

digits_B = []
while the_number:
    the_number, mod = divmod(the_number, B)
    digits_B.append(mod)
print(*digits_B[::-1], end=' ')