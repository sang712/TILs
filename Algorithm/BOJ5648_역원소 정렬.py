"""
길이 값을 따로 두어 입력을 받아올 때마다 길이를 재는 것이 아니라 
길이를 바로바로 비교할 수 있도록 하였음
그래서 현재 길이가 입력될 길이 값보다 같거나 크면 입력을 그만두고
입력된 값들을 뒤집고 정렬해서 출력하도록 하였음
"""
import sys
input = sys.stdin.readline

N, *eles = input().split()
N = int(N)
length = len(eles)
while length < N:
    new_eles = list(input().split())
    eles.extend(new_eles)
    length += len(new_eles)
    
print(*sorted(map(lambda x: int(x[::-1]), eles)), sep='\n')