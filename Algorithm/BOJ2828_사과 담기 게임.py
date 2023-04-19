"""
가장 처음에 바구니는 왼쪽에서 M칸을 차지하고 있다는 점을 확인하면 쉽게 풀리는 문제
바구니에서 벗어난 사과가 있을 때만 바구니를 움직여서
바구니의 왼쪽에 사과가 있다면 바구니의 시작점과 일치하도록
바구니의 오른쪽에 사과가 있다면 바구니의 끝점과 일치하도록 움직이게 하였음
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

start, end = 1, M
total_move = 0
for _ in range(int(input())):
    apple = int(input())
    move = 0
    if apple < start:
        move = start - apple
    elif end < apple:
        move = end - apple
    
    start -= move
    end -= move
    total_move += abs(move)

print(total_move)