"""
문제를 이해하기 어려워서 힘들었는데
O(g(n))의 정의에 따라서
g(n) = n일 때 정의가 만족하는지 확인하면 되는 문제였음

정리를 하면 a0 <= (c-a1)*n0을 만족하면 전체가 만족한다는 것인데
여기서 중요한 것은 c-a1이 음수가 되면 값이 음으로 가기 때문에 
어느 순간에 가서는 만족하지 않다는 것임
"""
a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if c-a1 < 0:
    print(0)
elif (c-a1)*n0 >= a0:
    print(1)
else:
    print(0)
