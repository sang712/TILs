"""
소수를 구해서 나눈 다음 인수를 구할까 생각을 했는데
차라리 소수를 구하는 에라토스테네스의 체 방식으로 카운팅을 해버리자 생각을 해서
제한조건의 크기의 배열을 하나 만들어
그냥 배수를 카운팅 한 뒤에 자기자신에 해당하는 카운팅 1을 빼고 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]

counter = {}
for num in sorted(nums):
    counter.setdefault(num, 0)
    counter[num] += 1
    
toktoks = [0] * 1_000_001
for num, cnt in counter.items():
    for multi_num in range(num, 1_000_001, num):
        toktoks[multi_num] += cnt
        
ans = []
for num in nums:
    ans.append(toktoks[num] - 1)
print(*ans, sep='\n')