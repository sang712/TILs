'''
A를 list로 하여서 in 방식으로 탐색할 때 O(N)만큼 소요되어 시간 초과가 났음
A를 set으로 하여 문제 해결
'''
N = int(input())
A = set(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
  print(1) if num in A else print(0)
