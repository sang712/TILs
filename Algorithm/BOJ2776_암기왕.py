"""
set 자료구조를 이용해 등장한 숫자를 저장하였고
등장했다고 한 숫자와 일치하면 list 자료 구조에 저장하였음
"""
import sys
input = sys.stdin.readline
for t in range(int(input())):
    N = int(input())
    note1 = list(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))
    counter = set()
    for num in note1:
        counter.add(num)
    
    ans = []
    for num in note2:
        has_been_seen = 0
        if num in counter:
            has_been_seen = 1
        ans.append(has_been_seen)
    
    print(*ans, sep='\n')