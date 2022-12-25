'''
BOJ15652 N과 M (4) 문제와 같은 방법으로 풀었으며, 
이 문제에서는 숫자를 따로 주기 때문에 숫자를 받아 정렬한 뒤 사용하였음
'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

def make_squence(sequence: list[int], i: int) -> None:
    if len(sequence) == M:
        print(*sequence)
        return
    
    for idx in range(i, len(nums)):
        sequence.append(nums[idx])
        make_squence(sequence, idx)
        sequence.pop()

make_squence([], 0)