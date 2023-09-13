"""
풀기 전에는 어떻게 풀어야하나 막막했지만 생각의 흐름대로 짜고 나니 쉽게 풀렸던 문제
숫자를 1부터 1씩 증가시키면서 각 자리수를 N[idx]와 비교하고 
서로 같을 때 idx를 1씩 증가하는 방식으로 풀이하였음
"""
N = input()

len_N = len(N)
num = 1
idx = 0
while idx < len_N:
    for i in str(num):
        if N[idx] == i:
            idx += 1
        if idx >= len_N:
            break
    else:
        num += 1
print(num)