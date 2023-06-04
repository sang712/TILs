"""
전혀 알지 못하는 언어라는 점을 제외하고는 쉽게 풀 수 있었음
입력의 절반 길이에 해당하는 윈도우에
N번을 반복하면서 파란구슬이 최대로 들어오는 경우를 찾도록 풀이하였음
"""
necklace = list(input())
N = len(necklace)
max_blue = num_blue = sum(map(lambda x: x=='B', necklace[N//2:N]))
for i in range(N):
    if necklace[i] == 'B':
        num_blue += 1
    
    if necklace[(i + N//2) % N] == 'B':
        num_blue -= 1
    
    if num_blue > max_blue:
        max_blue = num_blue
    
print(max_blue)