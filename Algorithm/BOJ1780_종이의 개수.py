"""
재귀를 이용한 분할정복을 이용하여 문제를 풀이하였음

재귀로 타고 들어가는 함수를 구현하였는데 받는 인자로는 좌표와 종이의 크기로 정했음
종이의 크기가 1일 경우에는 바로 그 숫자를 반환하도록 했고
그렇지 않을 경우에는 3*3 으로 종이의 숫자를 카운트한 뒤에 카운트 한 숫자가 9라면
해당 숫자를 반환하도록 하였음 대신 이 때 사이즈가 종이의 크기와 같으면 최종적으로 1번 더해주도록 하였음
카운트 한 숫자에 9가 없다면 카운트한 숫자만큼 최종 카운트에 더하도록 하였음
"""
import sys
input = sys.stdin.readline

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

total_paper_count = [0] * 4

def check_paper(r: int, c:  int, n: int) -> int:
    if n == 1:
        return paper[r][c]
    
    paper_count = [0] * 4
    
    gap = n//3
    for i in range(3):
        for j in range(3):
            num_paper = check_paper(r+i*gap, c+j*gap, gap)
            paper_count[num_paper + 1] += 1
            
    for i in range(3):
        if paper_count[i] == 9:
            if n == N:
                total_paper_count[i] += 1
            return i -1
        else:
            total_paper_count[i] += paper_count[i]
    return 2

check_paper(0, 0, N)
print(*total_paper_count[:-1], sep='\n')
        
    