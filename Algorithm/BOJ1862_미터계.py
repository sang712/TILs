"""
원래 주어진 수에서 수를 빼는 방식으로 하려고 했는데 고려할 것이 많아서 
더하는 방식으로 수정하여 풀이하였음
각 자릿수별로 4보다 작은 수면 9의 자릿수 승만큼 곱하고
4보다 큰 수면 해당 수에 1을 빼고 9의 자릿수 승만큼 곱하는 방식으로 계산하여 답을 내었음
"""
N = input()
ans = 0
for i in range(len(N)):
    digit = int(N[len(N)-1-i])
    gap = int(9 ** i)
    if digit < 4:
        ans += gap * digit
    else:
        ans += gap * (digit-1)
print(ans)