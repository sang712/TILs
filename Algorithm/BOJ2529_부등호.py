"""
재귀 함수로 수를 정해서 부등호에 맞으면 다음 자리수로 넘어가는 방식을 이용해 구현하였음
작은 수부터 확인하여 최소 정수를, 큰 수부터 확인하여 최대 정수를 구하였음
"""
N = int(input())
signs = input().split()

def compare(num1, sign, num2):
    if sign == '<':
        if num1 < num2:
            return True
    elif sign == '>':
        if num1 > num2:
            return True
    return False

def make_sequence(num: list, reverse: bool = False):
    l = len(num)    
    if l > N:
        return ''.join(map(str, num))
    
    ans = None
    if reverse:
        for i in range(9, -1, -1):
            if not selected[i] and compare(num[-1], signs[l-1] ,i):
                selected[i] = 1
                ans = make_sequence(num + [i], reverse)
                selected[i] = 0
            if ans:
                return ans
    else:
        for i in range(10):
            if not selected[i] and compare(num[-1], signs[l-1] ,i):
                selected[i] = 1
                ans = make_sequence(num + [i], reverse)
                selected[i] = 0
            if ans:
                return ans

selected = [0] * 10
for i in range(10):
    selected[i] = 1
    min_ans = make_sequence([i])
    selected[i] = 0
    if min_ans:
        break

for i in range(9, -1, -1):
    selected[i] = 1
    max_ans = make_sequence([i], True)
    selected[i] = 0
    if max_ans:
        break

print(max_ans, min_ans, sep='\n')