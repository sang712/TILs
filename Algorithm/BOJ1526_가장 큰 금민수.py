"""
4미만일 때, 4일 때, 7미만일 때, 7일 때, 7초과일 때를 나누어 풀이하였음

풀이하면서 찾은 반례로 각각의 조건을 찾도록 해주었음
4433 4미만일 때 처리를 하는 방법
473 4미만인데 그 직전 값으로 결정된 값이 7일 때 처리를 하는 방법
450 4초과 7미만일 때 처리를 하는 방법
"""
N = input()

number = []

for i in range(len(N)):
    if N[i] < '4':
        for j in range(len(number) - 1, -1, -1):
            if number[j] == '4':
                number[j] = '7'
            elif number[j] == '7':
                number[j] = '4'
                if i - j == 1:
                    number.append('7')
                break
        for _ in range(len(N) - i - 1):
            number.append('7')
        else:
            break
    elif N[i] == '4':
        number.append('4')
    elif N[i] > '7':
        for _ in range(len(N) - i):
            number.append('7')
        else:
            break
    elif N[i] == '7':
        number.append('7')
    else:
        number.append('4')
        for _ in range(len(N) - i - 1):
            number.append('7')
        else:
            break
        
print(''.join(number))

"""
def minsu(A):
    res = A
    if A * 10 + 4 <= N:
        res = max(res, minsu(A * 10 + 4))
    if A * 10 + 7 <= N:
        res = max(res, minsu(A * 10 + 7))
    return res

N = int(input())
print(minsu(0))
"""

"""
import itertools

arr=[]

for i in range(1,7):
    a = list(map(''.join, itertools.product((['4','7']), repeat=i)))
    for j in a:
        arr.append(j)
        
arr=reversed(list(map(int, arr)))

n=int(input())

for i in arr:
    if i>n:
        continue
    print(i)
    break
"""