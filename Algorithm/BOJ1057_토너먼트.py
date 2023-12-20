"""
두 선수의 번호의 크기가 서로 반대인 경우를 고려하지 않아서 틀린 답을 냈음
두 경우를 모두 고려해주도록 하였음
"""
N, kim, lim = map(int, input().split())

def victory(player):
    return (player + 1) // 2

round = 0
while N > 1:
    round += 1
    if kim % 2 and kim + 1 == lim or lim % 2 and lim + 1 == kim:
        print(round)
        break
    
    N = victory(N)
    kim = victory(kim)
    lim = victory(lim)
else:
    print(-1)
