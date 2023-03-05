"""
로프를 정렬하여 
견딜 수 있는 하중이 가장 낮은 로프부터 for 문으로 돌면서
해당 하중 * 해당 로프보다 견딜 수 있는 하중이 큰 로프의 개수를 곱해
해당 로프가 포함 되었을 때 견딜 수 있는 하중을 구했고
그 하중을 비교하면서 최대로 견딜 수 있는 하중을 구하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort()

max_weight = 0
num_ropes = len(ropes)
for i in range(num_ropes):
    weight = ropes[i] * (num_ropes - i)
    max_weight = max(max_weight, weight)

print(max_weight)