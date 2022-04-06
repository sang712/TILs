'''
유클리드 호제법을 이용해 gcd를 구하고
gcd를 이용해 lcm을 구한다
'''

def gcd(num1, num2):
    if num2 == 0: return num1
    else: return gcd(num2, num1 % num2)
    # 큰 수와 작은 수의 위치 상관 없이 이렇게 짜 두면 알아서 앞뒤가 바뀜


def solve():
    n1, n2 = map(int, input().split())
    num_gcd = gcd(n1, n2)
    print(num_gcd)
    print(n1 * n2 // num_gcd)

solve()