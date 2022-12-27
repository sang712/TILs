'''
나눗셈의 분배법칙을 이용해서 구하는 문제라니 정말 감탄만 나왔음
더하기 전에 나누든 더한 후에 나누든 똑같으니 말이다 해당 방법으로 구현해보겠음

숫자의 쌍이 겹치는 부분이 있어서 경우의 수가 그렇게 많지 않을 거라 판단하였고
경우의 수를 다 따져서 if 분기로 처리하였음

처음에 print에 i를 넣어서 3%에서 틀렸고
마지막에 숫자 3개인 경우를 고려하지 않아서 100%에서 틀렸음

그리고 코드를 더 짧게 만들겠답시고 for i for j 해서 possibility를 돌면서 나머지가 4인지 확인하는 로직으로 바꿨는데
그냥 possibilities의 경우를 다 안 따지고 최대로 많을 때만의 경우를 따져서 86%에서 실패하였음

다른 풀이를 찾아본 결과 dfs를 이용하였던데 나중에 시간이 되면 dfs로 구현해보도록 해야겠음
푼 사람도 많이 없는지라 하드코딩(??)으로 36ms라는 시간으로 1등하였음

그냥 dfs로 구현해보자 해서 바로 구현했더니 이것도 36ms가 나왔음..??
'''
N = int(input())
A = list(map(int, input().split()))

possibilities = [0] * 7

for Ai in A:
    remainder = Ai % 7
    possibilities[remainder] += 1
    
condition = [0, 4, 2, 6, 1, 5, 3] # 넘어가면 바로 나누어 떨어짐

def DFS(n, day):
    if day % 7 == 4:
        print('YES')
        return True
    
    if n >= 7:
        return False
    
    if DFS(n + 1, day):
        return True
    
    for _ in range(possibilities[n]):
        day += n
        if DFS(n + 1, day % 7):
            return True

if not DFS(1, 0):
    print('NO')
    
def solution():
    for i in range(1, 7):
        if possibilities[i] >= condition[i]:
            print('YES')
            return
    p0, p1, p2, p3, p4, p5, p6 = possibilities
    if p1 >= 1 and (p3 >= 1 or p5 >= 2):
        print('YES')
        return
    elif p1 >= 2 and p2 >= 1:
        print('YES')
        return
    elif p2 >= 1 and p3 >= 3:
        print('YES')
        return
    elif p3 >= 1 and p5 >= 3:
        print('YES')
        return
    elif p3 >= 2 and (p5 >= 1 or p6 >= 2):
        print('YES')
        return
    elif p6 >= 1 and (p3 >= 4 or p5 >= 1):
        print('YES')
        return
    elif p2 and p3 and p6:
        print('YES')
        return
    print('NO')
# solution()