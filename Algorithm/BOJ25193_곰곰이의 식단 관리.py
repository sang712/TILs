'''
math를 import하기 귀찮아서 0.5를 더하고 round를 했는데 반례가 여러개 생겼음
그 중에 하나가 
1
C
인데 0.5를 더하고 round를 하면 2가 돼 버려서 딱 나누어 떨어지는 경우에 다음 수로 넘겨버리는 경우가 있었던 거 같음
ceil을 사용하여 해당 문제를 해결하였음
'''
import math

N = int(input())
S = input()

num_chickens = S.count('C')
other_foods = N - num_chickens

print(math.ceil((num_chickens / (other_foods + 1))))