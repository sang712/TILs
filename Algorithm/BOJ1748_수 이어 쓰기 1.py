'''
자리수를 len으로 가져와서 이용하였고 
N과 1로 시작하여 그 외의 모든 자리수가 0인 수와의 차이가
해당 자리수인 숫자의 개수 이므로 이를 gap으로 계산하였음
그러고 자리수와 숫자의 개수의 곱을 answer에 더해주었고 이를 계속 반복하였음
'''
N = input()
answer = 0
while int(N):
    num_digit = len(N)
    gap = int(N) - (10 ** (num_digit-1)) + 1
    answer += gap * num_digit
    N = str(int(N)-gap)
print(answer)
