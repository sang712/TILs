"""
각 수 별로 나올 수 있는 경우를 문자열로 만들어 2차원 리스트에 저장하였음
1 2 3의 경우를 초기값으로 갖고 그 후에는 직전 3개의 경우에 +1, +2, +3을 하여 구한뒤
정렬을하고 append 하는 방식으로 풀이하였음

스트링 연산이기 때문에 n의 범위가 조금만 더 커져도 시간소요가 클 것으로 예상되는데
이 풀이는 36ms밖에 걸리지 않았음
"""
n, k = map(int, input().split())

seqs = [['1'], ['1+1', '2'], ['1+1+1', '1+2', '2+1', '3']]

for i in range(3, n):
    temp = []
    for seq in seqs[i-1]:
        temp.append(seq+'+1')
    for seq in seqs[i-2]:
        temp.append(seq+'+2')
    for seq in seqs[i-3]:
        temp.append(seq+'+3')
    seqs.append(sorted(temp))

seq_n = seqs[n-1]
if k <= len(seq_n):
    print(seq_n[k-1])
else:
    print(-1)