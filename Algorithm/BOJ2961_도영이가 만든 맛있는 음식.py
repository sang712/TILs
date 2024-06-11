"""
인덱스를 인자로 갖는 재귀함수를 이용해 재료를 선택/비선택 하는 경우를 나누었고
글로벌 키워드를 이용해 언제든 답을 초기화할 수 있도록 했으며
최소한의 재료를 1개 이상 택했을 때 답을 초기화하도록 하였음
"""
N = int(input())
ingredient = [list(map(int, input().split())) for _ in range(N)]

def take_or_not(i, sour, bitter):
    global ans
    if not (sour == 1 and bitter == 0):
        ans = min(ans, abs(sour-bitter))
    if i >= N:
        return
    
    take_or_not(i+1, sour, bitter)
    take_or_not(i+1, sour*ingredient[i][0], bitter+ingredient[i][1])
    
ans = 1_000_000_000
take_or_not(0, 1, 0)
print(ans)