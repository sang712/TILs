"""
처음에 패턴을 그려놓고 접근하는 방식으로 접근했는데 어떻게 해도 메모리 초과가 났음
그래서 좌표로 알파벳을 계산하는 방식을 검색을 통해 찾았음
a의 위치를 기점으로 거리를 재서 알파벳을 배정하는 방식임

+) 추가로 abcd에 리스트(혹은 스트링) 리버스+슬라이싱으로 cba를 붙이려면 List + List[-2::-1] 해야한다는 것
    거꾸로 뒤집어서 시작할 때 시작점이 마지막에서 2번째 거부터 시작하기 때문
"""
N, R1, C1, R2, C2 = map(int, input().split())

width = 2*N - 1
ans = []
for i in range(R1, R2+1):
    row = []
    for j in range(C1, C2+1):
        i %= width
        j %= width
        dist = abs(N-1 - i) + abs(N-1 - j)
        
        if dist >= N:
            row.append('.')
        else:
            row.append(chr(ord('a') + dist % 26))
    ans.append(''.join(row))
print(*ans, sep='\n')