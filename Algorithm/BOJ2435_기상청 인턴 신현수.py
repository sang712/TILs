'''
부분 합을 구한 리스트를 만들어서 
첫 값을 빼고 끝 값을 더하는 방식으로 
각 부분합을 초기화 하고 최댓값을 가져옴
'''
N, K = map(int, input().split())
temperature = list(map(int, input().split()))
sumation = [0 for _ in range(N-K+1)]

max_temp = 0
for i in range(N-K+1):
    if i == 0:
        for j in range(K):
            sumation[i] += temperature[j]
        max_temp = sumation[i]
    else:
        temp_sum = sumation[i-1] - temperature[i-1] + temperature[i+K-1]
        max_temp = max(max_temp, temp_sum)
        sumation[i] = temp_sum

print(max_temp)
