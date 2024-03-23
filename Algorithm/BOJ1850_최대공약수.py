"""
1로만 이루어진 두 수의 최대 공약수의 1의 개수를 
1의 개수를 수로 나타냈을 때의 두 수의 최대공약수로 나타낼 수 있어서 
입력을 받아 바로 최대공약수를 구했고 여기에 '1'을 곱해 출력함으로써 풀이하였음
"""
a, b = map(int, input().split())
def gcd(num1, num2):
    if num2 == 0: return num1
    else: return gcd(num2, num1%num2)
print('1'*gcd(a, b))