"""
연속해서 사용하는 시간과 연속해서 사용하지 않는 시간을 카운팅 하고
사용중 이라는 상태는 다른 변수로 저장하였음
그 후에 연속해서 사용하지 않는 시간이 L이상이고 사용중이면 해당 시각을 저장하도록하였음
마지막에 사용중 상태로 끝났을 경우 L만큼 시간을 더해서 답을 구하였음
"""
K, L, N = map(int, input().split())
data = input()
using = 0
used = False
done = 0
ans = []
for i, datum in enumerate(data):
    if datum == '1':
        using += 1
        done = 0
    if using >= K:
        used = True
    if datum == '0':
        done += 1
        using = 0
    if used and done >= L:
        used = False
        done = 0
        using = 0
        ans.append(i+1)
        
if used:
    ans.append(i+1+L-done)
print(*ans, sep='\n') if ans else print('NIKAD')