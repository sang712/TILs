'''
zip을 이용해서 원래의 위치를 저장하고 값을 기준으로 정렬하여 
그보다 작은 것들의 개수를 세었는데
시간이 3252ms 으로 너무 오래 걸려서 
set과 dictionary를 이용해보도록 하겠음
걸린 시간은 1896ms
set사용은 그대로 하되 dictionary를 사용하지 않고 마지막 반복문 2개를 
이분탐색으로 구현하면 더 빠르지 않을까 생각해 봄
'''
# zip을 이용하여 구현한 코드
'''
N = int(input())

Xs = list(map(int, input().split()))
idxs = [i for i in range(N)]

sorted_Xs = list(zip(Xs, idxs))
sorted_Xs.sort()

answer = ['0'] * N

prev = sorted_Xs[0][0]
answer[sorted_Xs[0][1]] = '0'

cnt = 0
for order in range(1, N):
    num, idx = sorted_Xs[order]
    if num == prev:
        answer[idx] = str(cnt)
    else:
        cnt += 1
        answer[idx] = str(cnt)
        prev = num
print(' '.join(answer))

'''

# set과 dictionary를 이용한 코드
N = int(input())
Xs = list(map(int, input().split()))

nonoverlap_Xs = list(set(Xs))
nonoverlap_Xs.sort()
count_Xs = {}

for idx, num in enumerate(nonoverlap_Xs):
    count_Xs.setdefault(num, idx)
answer = []
for i in range(N):
    answer.append(str(count_Xs[Xs[i]]))
    
print(' '.join(answer))