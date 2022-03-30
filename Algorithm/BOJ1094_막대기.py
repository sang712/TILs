'''
그냥 구현을 했음
1. 막대가 X보다 큰지 먼저 비교를 해야되는데 이 경우는 64인 경우 밖에 없어서 그냥 조건으로 넣었음
2. 그 외에는 주어진 조건을 따라 그대로 구현함

* 이진법으로 만들어서 1의 개수를 세는 방식도 있음
'''

X = int(input())

length = 64
stick = 64
nums = 1

while True:
    if X == 64:
        print(nums)
        break
    stick //= 2
    nums += 1
    if length - stick >= X:
        length -= stick
        nums -= 1
    if length == X:
        print(nums)
        break
