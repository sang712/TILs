"""
보기에 불편하지만 4중 for문을 적용하여 문제를 풀이하였음
"""
N = int(input())
cherryblossom = list(map(int, input().split()))

def grouping(n):
    if type(n) is int:
        return n
    temp = 1
    for num in n:
        temp *= num
    return temp
max_P = 0
for i in range(N - 3):
    for j in range(i + 1, N - 2):
        for k in range(j + 1, N - 1):
            for l in range(k + 1, N):
                P = grouping(cherryblossom[i:j]) 
                P += grouping(cherryblossom[j:k])
                P += grouping(cherryblossom[k:l])
                P += grouping(cherryblossom[l:])
                max_P = max(P, max_P)
print(max_P)