import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    string = input().strip()
    print(string[0]+string[-1])