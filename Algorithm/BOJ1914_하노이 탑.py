"""
재귀로 문제를 풀었음
나머지 한 칸을 구하는 방법을 list, set을 이용하지 않고 그냥 if문으로 처리했으면 더 빠른 속도가 나왔을 것
"""
N = int(input())

move_record = []
def move(start, end, block):
    if block > 1:
        new_end = list(set([1, 2, 3]) - set([start, end]))[0]
        move(start, new_end, block-1)
    move_record.append(f'{start} {end}')
    if block > 1:
        move(new_end, end, block-1)
    
print(2**N-1)
if N <= 20:
    move(1, 3, N)
    print(*move_record, sep='\n')