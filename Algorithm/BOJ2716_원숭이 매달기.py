"""
그냥 입력을 for문으로 돌면서 왼쪽 괄호면 줄기가 한 번 나눠졌다는 뜻이므로 깊이 1을 더했고
오른쪽 괄호면 나눠진 줄기가 더는 없다는 뜻으로 깊이 1을 뺐음
그 후에 최대로 나누어진 줄기의 개수를 2의 지수로 하여 답을 출력하였음
"""
import sys
input = sys.stdin.readline
N = int(input())

for tc in range(N):
    vine = input()
    max_depth = depth = 0
    
    for stem in vine:
        if stem == '[':
            depth += 1
            if max_depth < depth:
                max_depth = depth
        elif stem == ']':
            depth -= 1
            
    print(2**max_depth)