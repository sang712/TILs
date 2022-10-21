'''
조건
1 ≤ N ≤ 3×103 인 정수
1 ≤ Ai ≤ 108 인 정수

풀이
N^2이 9백만이라서 O(N^2)방법으로 풀어도 무난한 문제
근데 첫 접근 방법이 틀렸다
전 단계 까지의 높이와 건너온 돌들의 개수를 카운트 해서 비교했더니 
중간에 건너뛰어지는 부분이 있어서 틀렸었음
그래서 찾아본 결과 dp 형식으로 모든 원소에 1을 넣어 초기화하고
for문을 돌면서 해당 인덱스 이전의 dp값의 최대값을 해당 인덱스에 초기화하는 방식
'''


import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

chosen = [1]*(N+1)

for i in range(1, N):
    max_chosen = 0
    for j in range(i):
        if A[i] > A[j]:
            max_chosen = max(max_chosen, chosen[j])
    chosen[i] = max_chosen + 1
print(max(chosen))