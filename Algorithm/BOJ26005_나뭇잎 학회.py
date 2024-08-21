"""
n*n 칸을 2칸씩 모두 덮을 수 있는 횟수를
구하면 된다고 생각하여 그렇게 풀이함
"""
n = int(input())

if n <= 1:
    print(0)
else:
    print((n**2+1)//2)