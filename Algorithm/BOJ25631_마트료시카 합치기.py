"""
어제 공부했던 대로
visited에 리스트를 사용하는 대신
비트 마스킹을 적용해보았음
비트마스킹 풀이는 왠지모르게 시간이 130ms가 걸려서
방문체크를 안 하도록 그냥 pop시켜버렸음
그 결과는 84ms 어떤 방법으로 풀어야 40ms가 나오는지 모르겠음
"""
N = ans = int(input())
ai = list(map(int, input().split()))
ai.sort()

bigger = ai.pop()
checked = 0
while ai:
    checked += 1
    for j in range(N-checked-1, -1, -1):
        if ai[j] < bigger:
            bigger = ai.pop(j)
            ans -= 1
            break
    else:
        bigger = ai.pop()
        
print(ans)