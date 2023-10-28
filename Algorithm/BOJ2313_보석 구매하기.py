"""
누적합 문제인데 음수가 포함되어있어서 조금 어려웠음
음수가 포함된 누적합 문제를 처음 접해서 그런 것 같음
누적합으로 해놓고 2중 for문을 쓰려고 해서 시간초과가 났고
누적합을 제대로 적용했는데 가능한 범위를 고려하지 않아서 한 번 더 인덱스에러가 나서 틀렸음

최대가 0보다 크면이라고 잡았기 때문에 
음수 보석 1개만 존재할 때 serial_jewels 리스트에 넣질 않아서 생긴 문제였음
처음 최댓값을 -10000로 초기화해서 통과할 수 있었음
"""
n = int(input())

ans = [0]
for tc in range(n):
    L = int(input())
    jewels = list(map(int, input().split()))
    
    acc = [0]
    
    sumation = 0
    for i in range(L):
        sumation += jewels[i]
        acc.append(sumation)
    
    serial_jewels = []
    max_serial = -10000
    end = 0
    min_value, min_idx = 0, 0
    while end < L:
        end += 1
        if min_value >= acc[end - 1]:
            min_value = acc[end - 1]
            min_idx = end - 1
        
        if max_serial < acc[end] - min_value:
            max_serial = acc[end] - min_value
            serial_jewels = [(min_idx, end)]
        elif max_serial == acc[end] - min_value:
            serial_jewels.append((min_idx, end))
            
    ans[0] += max_serial
    
    serial_jewels.sort(key=lambda x: (x[1] - x[0], x[0], x[1]))
    ans.append(str(serial_jewels[0][0] + 1) + ' ' + str(serial_jewels[0][1]))
    
print(*ans, sep='\n')