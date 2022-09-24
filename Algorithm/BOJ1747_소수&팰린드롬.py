'''
소수를 판단하고 팰린드롬을 판단하여 출력
소수 판정보다 팰린드롬 판정이 더 빨리 끝나기 때문에
if문으로 나눌 때 팰린드롬 판정을 앞에 두면 결과가 더 빨리 끝남
(pypy3기준 988ms 에서 196ms로)
+) n 이 1,000,000일 때 결과 값이 1003001을 계산 결과로 얻을 수 있어서
결과가 나오지 않았을 땐 1003001을 자동으로 출력하도록 하였음
그럼 1000000이하의 가장 큰 팰린&소수가 궁금하여 직접 일일이 찾아봤더니 98689
98690이상을 N으로 입력하면 1003001이 나옴
그래서 N의 범위를 98690까지로 줄였더니 python3기준 72ms로 줄음
'''
N = int(input())

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    n = str(n)
    return True if n == n[::-1] else False

def solve(n):
    for i in range(n, 98690):
        if is_palindrome(i) and is_prime(i):
            print(i)
            return
    else:
        print(1003001)

solve(N)