"""
그냥 딱 반으로 한 번만 접어서 확인하면 되는 줄 알았는데
반 접고 반 접고 해서 길이가 1이 될 때까지 확인하면 되었음
"""
import sys
input = sys.stdin.readline
T = int(input())

def fold(paper):
    length = len(paper)
    if length > 1:
        for i in range(length//2):
            if paper[i] == paper[-i-1]:
                break
        else:
            return fold(paper[:i+1])
        return 'NO'
    return 'YES'

for t in range(T):
    paper = input().strip()
    print(fold(paper))