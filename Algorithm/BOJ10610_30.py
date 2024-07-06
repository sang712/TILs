"""
문제에서 원하는 내용을 만족하려면
N에 0이 포함되면서 3의 배수를 만족하면 되고
이 조건을 만족하면 그냥 내림차순으로 정렬하여 출력하면 됨
"""
N = input()
if sum(map(int, N)) % 3 == 0 and '0' in N:
    print(''.join(sorted(list(N), reverse=True)))
else: 
    print(-1)