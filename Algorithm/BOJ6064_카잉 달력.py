"""
답은 M이나 N의 배수에 x 또는 y를 더하면 된다는 사실을 알게 되어서 해당 방법으로 구현하였음

다른 답을 찾아보니 공약수와 공배수를 찾아서 하는 방식이 있던데 100배 가까이 빠른 방법이었음
풀이를 여전히 이해하진 못해서 풀이에 옮기지는 않겠음
"""
import sys
input = sys.stdin.readline

for tc in range(int(input())):
    M, N, x, y = map(int, input().split())
    
    jump = 0
    answer = -1
    while True:
        year = M * jump + x
        if year % N == y or year % N == 0 and N == y:
            answer = year
            break
        if jump == N:
            break
        jump += 1
        
    print(answer)
    