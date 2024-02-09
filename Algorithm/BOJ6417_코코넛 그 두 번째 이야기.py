"""
1을 뺐을 때의 나누어 떨어지는 몫이 답이 될 수 있는 K임을 깨달아서 그걸 우선적으로 리스트에 저장했고
그 수들을 돌면서 직접 계산이 되는지 재귀함수로 돌려보도록 하였음
주의할 점은 코코넛을 원숭이한테 줬을 때 0개가 남아도 나누어 가질 수 있다고 본다는 점임
"""
def devide(coconuts, K, k):
    if k == 0:
        return True
    if (coconuts-1) % K == 0:
        return devide((coconuts-1)*(K-1)//K, K, k-1)
    else:
        return False

while True:
    coconuts = int(input())
    if coconuts == -1:
        break

    possible_k = []
    for i in range(2, max(int((coconuts-1)**0.5), 5)):
        if (coconuts-1) % i == 0:
            possible_k.append(i)
    
    for k in possible_k[::-1]:
        if devide(coconuts, k, k):
            print(f'{coconuts} coconuts, {k} people and 1 monkey')
            break
    else:
        print(f'{coconuts} coconuts, no solution')
